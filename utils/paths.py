"""
paths.py

Defines important project paths used throughout the framework.
"""

from pathlib import Path

# Root directory of the project (two levels up from this file)
PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT / "data"
TESTS_DIR = PROJECT_ROOT / "tests"

# Test reports
VIDEOS_DIR = TESTS_DIR / "videos"
TRACES_DIR = TESTS_DIR / "traces"
ALLURE_PATH = TESTS_DIR / "allure-results"
TESTS_REPORT_PATH = TESTS_DIR / "tests_report.json"
LOGS_PATH = TESTS_DIR / "logs"
AI_REPORTS_PATH = TESTS_DIR / "ai_reports"
