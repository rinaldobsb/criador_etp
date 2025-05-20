import flet as ft
from agent import recebe_dados
from pages.login import Login
from pages.formulario import Projeto
from pages.resultado import Resultado
from etp import ETP_Document
from db import create_database, connect_database, Users, ETP
from my_path import my_path



def initial():
    arq = my_path / "database.db"
    if not arq.exists():
        return create_database("database")
    else:
        return connect_database("database")


def main(page: ft.Page):
    login = Login(users=Users, engine=initial())
    projeto = Projeto(
                    doc_etp=ETP_Document,
                    engine=initial(),
                    etp=ETP,
                    recebe_dados=recebe_dados
                )
    page.views.clear()
    page.views.append(login)

    def route_change(event):
        if page.route == "/projeto":
            page.views.clear()
            page.views.append(
                projeto
            )
        elif page.route == "/resultado":
            page.views.clear()
            page.views.append(Resultado(page.session.get("id_etp")))
        page.update()

    def view_pop(event):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    #page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == "__main__":
    ft.app(main, assets_dir="assets")
