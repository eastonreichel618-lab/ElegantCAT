from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Literal

import librosa
import numpy as np
import torch

from .paths import V2L_ROOT, V2S_ROOT

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
if DEVICE == 'cuda':
    torch.backends.cudnn.benchmark = True

ModelName = Literal['v2L', 'v2S']


def available_models() -> list[str]:
    return ['v2L', 'v2S']


class ElegantCATModel:
    def __init__(self, model_name: ModelName):
        self.model_name = model_name
        if model_name == 'v2L':
            self.root = V2L_ROOT
            self.payload = torch.load(self.root / 'artifacts' / 'ElegantCAT-v2L.pt', map_location='cpu')
        elif model_name == 'v2S':
            self.root = V2S_ROOT
            self.payload = torch.load(self.root / 'artifacts' / 'ElegantCAT-v2S.pt', map_location='cpu')
        else:
            raise ValueError(f'Unknown model: {model_name}')
        self.model = torch.jit.load(str(self.root / 'artifacts' / self.payload['scripted_path']), map_location=DEVICE)
        self.model.eval()
        if DEVICE == 'cuda':
            self.model = self.model.half()

    def _predict_v2l(self, path: Path) -> dict:
        y, _ = librosa.load(str(path), sr=self.payload['sample_rate'], mono=True)
        if len(y) == 0:
            y = np.zeros(self.payload['sample_rate'], dtype=np.float32)
        mel = librosa.feature.melspectrogram(y=y, sr=self.payload['sample_rate'], n_mels=self.payload['n_mels'], fmax=8000)
        mel = librosa.power_to_db(mel, ref=np.max).astype(np.float32)
        time_frames = self.payload['time_frames']
        if mel.shape[1] < time_frames:
            mel = np.pad(mel, ((0, 0), (0, time_frames - mel.shape[1])), mode='constant', constant_values=mel.min())
        else:
            mel = mel[:, :time_frames]
        mel = (mel - mel.mean()) / (mel.std() + 1e-6)
        x = torch.from_numpy(mel[None, None, :, :]).to(DEVICE)
        if DEVICE == 'cuda':
            x = x.half()
        with torch.inference_mode():
            probs = torch.softmax(self.model(x), dim=1).float().cpu().numpy()[0]
        return self._format_probs(probs)

    def _load_audio_v2s(self, path: Path) -> np.ndarray:
        import soundfile as sf
        import torchaudio
        y, sr = sf.read(str(path), always_2d=False)
        y = np.asarray(y, dtype=np.float32)
        if y.ndim > 1:
            y = y.mean(axis=1)
        target_sr = int(self.payload['sample_rate'])
        target_samples = int(self.payload['target_samples'])
        if sr != target_sr:
            y = torchaudio.functional.resample(torch.from_numpy(y), sr, target_sr).numpy()
        if len(y) >= target_samples:
            y = y[:target_samples]
        else:
            y = np.pad(y, (0, target_samples - len(y)))
        peak = max(float(np.max(np.abs(y))), 1e-6)
        return (y / peak).astype(np.float32)

    def _format_probs(self, probs: np.ndarray) -> dict:
        order = np.argsort(probs)[::-1]
        return {
            'model_name': self.payload.get('model_name', self.model_name),
            'top_prediction': self.payload['classes'][int(order[0])],
            'ranked_predictions': [
                {'label': self.payload['classes'][int(i)], 'probability': float(probs[i])}
                for i in order
            ],
        }

    def _predict_v2s(self, path: Path) -> dict:
        probs = None
        y = self._load_audio_v2s(path)
        x = torch.from_numpy(y[None, None, :]).to(DEVICE)
        if DEVICE == 'cuda':
            x = x.half()
        with torch.inference_mode():
            probs = torch.softmax(self.model(x), dim=1).float().cpu().numpy()[0]
        classes = self.payload['classes']
        idx = {label: i for i, label in enumerate(classes)}
        adjusted = probs.astype(np.float32).copy()
        if 'distress_aggression' in idx:
            adjusted[idx['distress_aggression']] *= 0.72
        for label, mult in {'alert_defensive': 1.18, 'social_positive': 1.12, 'maternal': 1.08, 'mating': 1.06}.items():
            if label in idx:
                adjusted[idx[label]] *= mult
        adjusted = np.clip(adjusted, 1e-9, None)
        adjusted /= adjusted.sum()
        return self._format_probs(adjusted)

    def predict(self, file: str | Path) -> dict:
        path = Path(file)
        if self.model_name == 'v2L':
            return self._predict_v2l(path)
        return self._predict_v2s(path)


@lru_cache(maxsize=None)
def load_model(model_name: ModelName) -> ElegantCATModel:
    return ElegantCATModel(model_name)
