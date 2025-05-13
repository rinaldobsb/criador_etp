from src.main import main
from agent import ETP_Document, ETP_Creator
import flet as ft

import tomllib

with open(".env.toml", mode="r") as file:
    configs = tomllib.load(file.read)


ft.app(main)