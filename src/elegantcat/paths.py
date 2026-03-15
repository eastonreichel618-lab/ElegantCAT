from __future__ import annotations

from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parents[1]
SERIES_ROOT = REPO_ROOT
V2L_ROOT = SERIES_ROOT / 'ElegantCAT-v2L'
V2S_ROOT = SERIES_ROOT / 'ElegantCAT-v2S'
