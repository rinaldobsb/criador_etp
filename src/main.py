import flet as ft


def main(page: ft.Page):
    check_item_clicked = lambda e: print(e)
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.SUNNY),
        leading_width=40,
        title=ft.Text("Criador de ETPs"),
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Configurações"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    nome_projeto = ft.TextField(label="Nome do Projeto")
    objetivo_projeto = ft.TextField(label="Objetivo do Projeto", multiline=True)
    descricao_problema = ft.TextField(label="Descrição do problema", multiline=True)
    botao_próximo = ft.ElevatedButton(text="Próximo")
    page.add(
        ft.Column(
            controls=[
                nome_projeto,
                objetivo_projeto,
                descricao_problema,
                botao_próximo
            ],
            expand=True,
        )
    )

ft.app(main)
