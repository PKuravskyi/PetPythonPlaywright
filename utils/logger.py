"""
logger.py

Provides a utility function to initialize and configure a logger for test runs.
Creates browser-specific log directories and stores logs with timestamps.
"""

import logging
import os
from datetime import datetime

from utils.paths import LOGS_PATH


def init_logger(test_name: str, browser_name: str) -> logging.Logger:
    """
    Initialize and configure a logger for a test run.

    Creates a log file under 'logs/<browser_name>' with a timestamped filename.
    Logs debug info to file and info-level logs to the console.

    Args:
        test_name (str): Name of the test, used in the log filename.
        browser_name (str): Browser name (e.g., "chromium", "firefox"), used to create subfolder.

    Returns:
        logging.Logger: Configured logger instance.
    """
    log_dir: str = os.path.join(LOGS_PATH, browser_name)
    os.makedirs(log_dir, exist_ok=True)

    log_path: str = os.path.join(
        log_dir, f"{test_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    )

    # Configure the logger
    logging.basicConfig(
        filename=log_path,
        format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)d - %(message)s",
        filemode="w+",
        level=logging.DEBUG,
        force=True,
    )

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)d - %(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(console_handler)

    return logger
