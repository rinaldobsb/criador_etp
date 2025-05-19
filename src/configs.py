import tomllib
from typing import Dict


def configurations(file) -> Dict[str, str]:
    with open(file=file, mode="r", encoding="utf-8") as conf:
        configs = tomllib.load(conf.read())
    return configs
