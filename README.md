# ElegantCAT Models

Importable wrappers for:
- `ElegantCAT-v2L`
- `ElegantCAT-v2S`

## Install
```powershell
cd C:\Users\Levit\.openclaw\workspace\Stuff\ElegantCAT-series\ElegantCAT-models
C:\Users\Levit\AppData\Local\Programs\Python\Python311\python.exe -m pip install -e .
```

## Python
```python
from elegantcat import load_model

v2l = load_model("v2L")
print(v2l.predict("C:/path/to/meow.wav"))

v2s = load_model("v2S")
print(v2s.predict("C:/path/to/meow.wav"))
```

## CLI
```powershell
elegantcat predict --model v2L --file C:\path\to\meow.wav
elegantcat predict --model v2S --file C:\path\to\meow.wav
```

## Paths
By default the package reads artifacts from:
- `ElegantCAT-series/ElegantCAT-v2L/artifacts`
- `ElegantCAT-series/ElegantCAT-v2S/artifacts`

If those folders move, update `src/elegantcat/paths.py`.
