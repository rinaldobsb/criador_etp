from src.main import main

# from agent import ETP_Document, ETP_Creator
import flet as ft

import tomllib

with open("src/.env.toml", mode="rb") as file:
    configs = tomllib.load(file)


ft.app(main)
