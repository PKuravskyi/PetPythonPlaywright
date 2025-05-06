"""
paths.py

Defines important project paths used throughout the framework.
"""

from pathlib import Path

# Root directory of the project (two levels up from this file)
PROJECT_ROOT = Path(__file__).parent.parent

# Path to the 'data' directory inside the project root
DATA_DIR = PROJECT_ROOT / "data"
