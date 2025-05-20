import tomllib
from typing import Dict


def configurations(file) -> Dict[str, str]:
    with open(file=file, mode="rb") as conf:
        configs = tomllib.load(conf)
    return configs
