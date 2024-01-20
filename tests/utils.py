from typing import Union
import json

def load_json_file(path: str) -> Union[dict, list]:
    """Import and load a JSON file."""
    try:
        with open(path) as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        print('There was an error with decoding JSON')
        return