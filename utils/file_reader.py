import json
from pathlib import Path

from utils.paths import DATA_DIR


def read_json(filename: str, folder: Path = DATA_DIR) -> dict:
    file_path = folder / filename
    with open(file_path) as file:
        return json.load(file)
