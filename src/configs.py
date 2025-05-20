import tomllib
from typing import Dict
import os


def configurations(file) -> Dict[str, str]:
    try:
        with open(file=file, mode="rb") as conf:
            configs = tomllib.load(conf)
    except Exception as e:
        configs = {
            "GEMINI_API": os.getenv("GEMINI_API"),
            "JINAREADER": os.getenv("JINAREADER")
        }
        print(e)
    return configs
