import flet as ft
from sqlmodel import Session, select

from db import ETP


class Resultado(ft.View):
    def __init__(self, id: int, engine):
        super().__init__()
        self.route = "/resultado"
        self.controls = self.build_page()
        self.appbar = self.build_appbar()
        self.engine = engine
        self.id = id

    def build_appbar(self):
        return ft.AppBar(
            leading=ft.Icon(name=ft.IconValue.EDIT_DOCUMENT),
            title=ft.Text("Gerador de ETPs"),
            actions=[
                ft.IconButton(icon=ft.IconValue.RETURN_ICON, on_click=self.voltar),
            ],
        )

    def voltar(self, event):
        event.page.route("/projeto")

    def build_page(self):
        return [self.build_resultado()]

    def build_resultado(self):
        with Session(self.engine) as session:
            statement = select(ETP).where(id_ = self.id)
            result = session.exec(statement)
        self.padding = ft.padding.symmetric(horizontal=80, vertical=100)
        texto_resultado = ft.Markdown(
            result.text_markdown,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: e.page.launch_url(e.data),
        )
        coluna = ft.Column(controls=[texto_resultado])
        return coluna
