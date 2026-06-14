"""Ensure repo root is importable so `src` and `run` resolve during tests."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
