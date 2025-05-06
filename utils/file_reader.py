"""
file_reader.py

Provides utility function to read JSON files from a specified folder.
"""

import json
from pathlib import Path

from utils.paths import DATA_DIR


def read_json(filename: str, folder: Path = DATA_DIR) -> dict:
    """
    Reads a JSON file and returns its content as a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read.
        folder (Path, optional): The folder where the JSON file is located. Defaults to DATA_DIR.

    Returns:
        dict: The content of the JSON file as a Python dictionary.
    """
    file_path = folder / filename
    with open(file_path, encoding="utf-8") as file:
        return json.load(file)
