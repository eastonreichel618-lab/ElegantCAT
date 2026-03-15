# ElegantCAT Models

Importable wrappers for:
- `ElegantCAT-v2L`
- `ElegantCAT-v2S`

## Install
```bash
pip install -e .
```

## Python
```python
from elegantcat import load_model

v2l = load_model("v2L")
print(v2l.predict("/path/to/meow.wav"))

v2s = load_model("v2S")
print(v2s.predict("/path/to/meow.wav"))
```

## CLI
```bash
elegantcat predict --model v2L --file /path/to/meow.wav
elegantcat predict --model v2S --file /path/to/meow.wav
```

## Benchmark stats
Primary quality benchmark is the 63-clip combined set.

### Combined 63 benchmark
- **ElegantCAT-v2L:** `0.8254 acc / 0.8289 macro / 18.28 ms`
- **ElegantCAT-v2S:** `0.7143 acc / 0.7120 macro / 12.68 ms`
- **cat-alan:** `0.6825 acc / 0.6586 macro / 8.53 ms`

### Pandeya 50 benchmark
- **ElegantCAT-v2L:** `0.78 acc / 0.7897 macro`
- **cat-alan:** `0.66 acc / 0.6390 macro`

### DynamicSuperb 13 benchmark
- **ElegantCAT-v2L:** `1.00 acc / 1.00 macro`
- **cat-alan:** `0.7692 acc / 0.6381 macro`

## Fast-path latency
When benchmark audio is normalized to canonical **16k mono WAV** and measured through the fast inference path:
- **ElegantCAT-v2S:** `~2.20 ms total`
- **cat-alan:** `~3.39 ms total`
- **ElegantCAT-v2L:** `~12.57 ms total`

This shows that `v2S` is the fast option when input format is controlled.

## Benchmark clips
Benchmark manifests are included in `benchmarks/`:
- `benchmarks/combined_benchmark.csv`
- `benchmarks/pandeya_bench.csv`
- `benchmarks/combined63_all_models.json`

## Paths
By default the package expects this repo to live alongside:
- `ElegantCAT-v2L/`
- `ElegantCAT-v2S/`

If your layout is different, update `src/elegantcat/paths.py`.
