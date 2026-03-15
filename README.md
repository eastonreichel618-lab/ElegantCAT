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

## Benchmark stats
Primary benchmark is the 63-clip combined set.

### Combined 63 benchmark
- **ElegantCAT-v2L:** `0.8254 acc / 0.8289 macro / 18.28 ms`
- **ElegantCAT-v1:** `0.7143 acc / 0.7120 macro / 15.29 ms`
- **ElegantCAT-v2S:** `0.7143 acc / 0.7120 macro / 12.68 ms`
- **cat-alan:** `0.6825 acc / 0.6586 macro / 8.53 ms`

### Pandeya 50 benchmark
- **ElegantCAT-v2L:** `0.78 acc / 0.7897 macro`
- **ElegantCAT-v1:** `0.68 acc / 0.6874 macro`
- **cat-alan:** `0.66 acc / 0.6390 macro`

### DynamicSuperb 13 benchmark
- **ElegantCAT-v2L:** `1.00 acc / 1.00 macro`
- **ElegantCAT-v1:** `0.8462 acc / 0.7738 macro`
- **cat-alan:** `0.7692 acc / 0.6381 macro`

## Benchmark clips
Benchmark manifests are included in `benchmarks/`:
- `benchmarks/combined_benchmark.csv`
- `benchmarks/pandeya_bench.csv`
- `benchmarks/combined63_all_models.json`

## Paths
By default the package reads artifacts from:
- `ElegantCAT-series/ElegantCAT-v2L/artifacts`
- `ElegantCAT-series/ElegantCAT-v2S/artifacts`

If those folders move, update `src/elegantcat/paths.py`.
