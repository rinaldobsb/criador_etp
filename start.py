from src.main import main
from agent import ETP_Document, ETP_Creator

import tomllib

with open(".env.toml", mode="r") as file:
    configs = tomllib.load(file.read)


