# ElegantCAT 🐱

**ElegantCAT** is a lightweight PyTorch model family for classifying cat vocalizations into multiple meow categories.
The project explores **efficient audio classifiers**, ranging from a higher-accuracy model (~1M parameters) to extremely small edge models (~30k parameters).

The dataset is built from publicly available repositories of cat vocalizations and uses **pseudo-labeling** to create training labels without manual annotation.

---

## Features

* PyTorch implementation
* 7-class cat vocalization classifier
* Model family with different parameter sizes
* Benchmarks on unseen cat clips
* Focus on **efficient inference**

---

## Models

| Model          | Params | Accuracy | Macro  | Latency  |
| -------------- | ------ | -------- | ------ | -------- |
| ElegantCAT-v2L | ~1M+   | 0.8254   | 0.8289 | 18.28 ms |
| ElegantCAT-v2S | ~30k   | WIP      | WIP    | TBD      |

**v2L** prioritizes classification performance.
**v2S** is an experimental tiny model designed for edge devices and extremely low compute environments.

---

## Benchmarks

### Unseen Cat Benchmark (63 clips)

| Model          | Accuracy | Macro  |
| -------------- | -------- | ------ |
| ElegantCAT-v2L | 0.8254   | 0.8289 |
| Cat-Alan       | 0.6825   | 0.6586 |

### Pandeya 50 Benchmark

| Model                     | Accuracy | Macro  |
| ------------------------- | -------- | ------ |
| ElegantCAT-v2S (expanded) | 0.60     | 0.6044 |

### 13 Clip Test Set

| Model                     | Accuracy | Macro  |
| ------------------------- | -------- | ------ |
| ElegantCAT-v2L            | 1.0      | 1.0    |
| ElegantCAT-v2S (expanded) | 0.6154   | 0.5769 |

Note: Some benchmarks are small and primarily used for quick evaluation.

---

## Dataset

Training data consists of approximately **2000 cat vocalization clips** gathered from publicly available repositories.

Labels are generated through **pseudo-labeling**, meaning no direct human annotation was used.
Because of this, labels reflect acoustic groupings rather than guaranteed semantic meaning.

---

## Training Pipeline

Typical pipeline:

Audio clip
→ Mel spectrogram
→ Convolutional neural network
→ 7-class classifier

Training is implemented in **PyTorch**.

---

## Goals

The project focuses on exploring:

* Efficient animal audio classifiers
* Model size vs performance tradeoffs
* Extremely small neural networks for audio tasks
* Fast experimentation using pseudo-labeled datasets

---

## Roadmap

* Improve **v2S tiny model**
* Experiment with **knowledge distillation from v2L**
* Expand evaluation benchmarks
* Improve robustness to different recording environments

---

## Status

Active development.

---

## License

MIT License

---

## Acknowledgements

Thanks to open repositories containing cat vocalization recordings that made building the dataset possible.
