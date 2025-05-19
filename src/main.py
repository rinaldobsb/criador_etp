import flet as ft
from agent import ETP_Creator
from pages.login import Login
from pages.formulario import Projeto
from pages.resultado import Resultado
from etp import ETP_Document
from db import create_database, connect_database, Users, ETP
from pathlib import Path
from bases_de_conhecimento import base_conhecimento, base_de_etps, base_de_leis

my_path = Path(".")


def initial():
    arq = my_path / "database.db"
    if not arq.exists():
        return create_database("database")
    else:
        return connect_database("database")


def main(page: ft.Page):
    engine = initial()
    page.views.clear()
    page.views.append(Login(users=Users, engine=engine))

    def route_change(event):
        troute = ft.TemplateRoute(page.route)
        if page.route == "/projeto":
            page.views.append(
                Projeto(
                    doc_etp=ETP_Document,
                    workflow_agent=ETP_Creator,
                    engine=engine,
                    etp=ETP,
                )
            )
        elif page.troute.match == "/resultado/:id":
            page.views.append(Resultado(troute.id))
        page.update()

    def view_pop(event):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == "__main__":
    base_de_leis.aload(skip_existing=True)
    base_de_etps.aload(skip_existing=True)
    base_conhecimento.aload(skip_existing=True)
    ft.app(main, assets_dir="assets")
