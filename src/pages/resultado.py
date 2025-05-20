import flet as ft
from sqlmodel import Session, select
from db import connect_database
from db import ETP


class Resultado(ft.View):
    def __init__(self, id_etp):
        super().__init__()
        self.route = "/resultado"
        self.id_etp = id_etp
        self.controls = self.build_resultado()
        self.appbar = self.build_appbar()
        self.scroll = ft.ScrollMode.AUTO

    def build_appbar(self):
        return ft.AppBar(
            leading=ft.Icon(name=ft.Icons.EDIT_DOCUMENT),
            title=ft.Text("Gerador de ETPs"),
            actions=[
                ft.IconButton(icon=ft.Icons.KEYBOARD_RETURN, on_click=self.voltar),
            ],
        )

    def voltar(self, event):
        event.page.route = "/projeto"
        event.page.go(event.page.route)

    # def did_mount(self):
    #     return self.build_resultado()

    def build_resultado(self):
        with Session(connect_database("database")) as session:
            statement1 = select(ETP.nome_do_projeto).where(ETP.id_ == self.id_etp)
            statement2 = select(ETP.text_markdown).where(ETP.id_ == self.id_etp)
            nome_do_projeto = session.exec(statement1).first()
            texto = session.exec(statement2).first()

        self.padding = ft.padding.symmetric(horizontal=80, vertical=100)
        titulo = ft.Text(value=f"Projeto de ETP: {nome_do_projeto}", size=25, weight=ft.FontWeight.BOLD)
        texto_resultado = ft.Markdown(
            value=texto,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: e.page.launch_url(e.data),
        )
        coluna = ft.Column(controls=[titulo, texto_resultado], spacing=15, scroll=ft.ScrollMode.AUTO)
        return [coluna]
