"""
file_reader.py

Provides utility function to read specific files from a specified folder.
"""

import csv
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


def read_csv(filename: str, folder: Path = DATA_DIR) -> list[dict]:
    """
    Reads a CSV file and returns its content as a list of dictionaries (each row as a dict).

    Args:
        filename (str): The name of the CSV file to read.
        folder (Path, optional): The folder where the CSV file is located. Defaults to DATA_DIR.

    Returns:
        list[dict]: A list where each item is a row from the CSV file as a dictionary.
    """
    file_path = folder / filename
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
