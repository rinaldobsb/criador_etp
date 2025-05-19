import flet as ft
from db import Users
from sqlmodel import select, Session


class Login(ft.View):
    def __init__(self, users: Users, engine):
        super().__init__()
        self.route = "/"
        self.controls = self.build_page()
        self.users = users
        self.engine = engine
        self.bgcolor = ft.Colors.TRANSPARENT
        self.decoration = ft.BoxDecoration(
            image=ft.DecorationImage(
                src="image_background.jpg", fit=ft.ImageFit.COVER, opacity=0.4
            ),
            bgcolor=ft.Colors.BLACK87,
        )
        self.padding = ft.padding.symmetric(vertical=100, horizontal=150)

    def build_page(self):
        self.username = ft.TextField(label="Username")
        self.password = ft.TextField(
            label="Password", password=True, can_reveal_password=True
        )
        login = ft.Column(
            controls=[
                ft.Text(
                    "Gerador de ETPs",
                    size=40,
                    animate_size=True,
                    text_align=ft.TextAlign.CENTER,
                ),
                self.username,
                self.password,
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Login", on_click=self.login_event),
                        ft.ElevatedButton("Cancel", on_click=self.cancel_event),
                    ]
                ),
            ],
            alignment=ft.alignment.center,
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            opacity=1,
        )
        return [login]

    def login_event(self, event):
        with Session(self.engine) as session:
            statement = select(self.users).where(self.username.value == self.users.user)
            result = session.exec(statement=statement)
            if result:
                if result.password == self.password:
                    event.page.route = "/projeto"
                else:
                    self.password.error_text = "Wrong password!"
                    event.page.update()
            else:
                self.username.error_text = "Wrong user!"
                event.page.update()

    def cancel_event(self, event):
        self.username.error_text = None
        self.username.value = ""
        self.password.error_text = None
        self.password.value = ""
        event.page.update()
