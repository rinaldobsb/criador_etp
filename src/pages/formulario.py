import flet as ft
from typing import Callable
from etp import ETP_Document
from db import ETP
from sqlmodel import Session, select


class Projeto(ft.View):
    def __init__(
        self, doc_etp: ETP_Document, engine, etp: ETP, recebe_dados: Callable
    ):
        super().__init__()
        self.route = "/projeto"
        self.controls = self.build_page(contexto="")
        self.appbar = self.build_appbar()
        self.doc_etp = doc_etp
        self.engine = engine
        self.db_etp = etp
        self.recebe_dados = recebe_dados
        self.scroll = ft.ScrollMode.AUTO

    def build_appbar(self):
        return ft.AppBar(
            leading=ft.Icon(name=ft.Icons.EDIT_DOCUMENT),
            title=ft.Text("Gerador de ETPs"),
            actions=[
                ft.IconButton(
                    icon=ft.Icons.EDIT, on_click=self.inicia_novo_projeto
                ),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text="Novo Projeto", on_click=self.inicia_novo_projeto
                        ),
                        ft.PopupMenuItem(
                            text="Projetos anteriores",
                            on_click=self.inicia_projetos_anteiores,
                        ),
                    ]
                ),
            ],
        )

    def inicia_novo_projeto(self, event):
        self.controls = self.build_page(contexto="novo")
        event.page.update()

    def inicia_projetos_anteiores(self, event):
        self.controls = self.build_page(contexto="anteriores")
        event.page.update()

    def inicia_em_branco(self, event):
        self.controls = self.build_page(contexto="")
        event.page.update()

    def build_page(self, contexto):
        if contexto == "novo":
            return [self.build_novo_projeto()]
        elif contexto == "anteriores":
            return [self.build_anteriores()]
        else:
            return [self.build_em_branco()]

    def build_em_branco(self):
        self.padding = ft.padding.symmetric(horizontal=80, vertical=100)
        texto_de_instrucao = ft.Text(
            value="Clique o botão Editar para criar um novo projeto de ETP",
            size=35,
            weight=ft.FontWeight.W_300,
        )
        coluna = ft.Column(controls=[texto_de_instrucao])
        return coluna

    def enviar_projeto(self, event):
        dlg = ft.AlertDialog(
            title=ft.Text("Aguarde a criação do ETP!"),
            content=ft.Text(
                "Os nossos agentes estão trabalhando na criação do ETP deste projeto. Aguarde."
            ),
            alignment=ft.alignment.center,
        )
        event.page.open(dlg)
        dados = [f.value for f in self.form]
        id_etp = self.recebe_dados(dados)
        event.page.session.set("di", id_etp)
        event.page.route = "/resultado/"

    def cancelar_projeto(self, event):
        for i in self.form:
            i.value = None
        self.inicia_em_branco()

    def build_novo_projeto(self):
        self.padding = ft.padding.symmetric(horizontal=60, vertical=40)
        self.form = [
            ft.TextField(label="Nome do Projeto"),
            ft.TextField(
                label="Objetivo do Projeto",
                multiline=True,
                helper_text="Descrição do objetivo do Documento, que é uma contratação de um bem ou de um serviço",
            ),
            ft.TextField(
                label="Os itens da Contratação",
                multiline=True,
                helper_text="Escreva os objetos da contratação da seguinte forma: (<nome>...<nome/> <descrição>...<descrição/> <quantidade>...<quantidade/>)",
            ),
            ft.TextField(
                label="Problema a ser resolvido",
                multiline=True,
                helper_text="Descrição dos problemas a serem resolvidos na contratação",
            ),
            ft.TextField(
                label="Necessidades de contratar",
                multiline=True,
                helper_text="Descreva as necessidades de contratar o bem ou serviço para resolver o problema",
            ),
            ft.TextField(
                label="Benefícios da Contratação",
                multiline=True,
                helper_text="Descreva os benefícios diretos e indiretos da contratação dos bens ouserviços do objetivo: <diretos>...<diretos/> <indiretos>...<indiretos/>",
            ),
            ft.TextField(
                label="Alinhamento da Contratação com os Planos Institucionais do Tribunal",
                multiline=True,
                helper_text="Descreve como a Contratação se alinha com a Resolução do CNJ e com o Plano Diretor do TRE-DF no seguinte formato: (<normativo>...<normativo/> <relação>...<relação/>)",
            ),
            ft.TextField(
                label="Requisitos Funcionais da Contratação",
                multiline=True,
                helper_text="Elenque os requisitos funcionais da Contratação",
            ),
            ft.TextField(
                label="Requisitos Não funcionais da Contratação",
                multiline=True,
                helper_text="Requisitos Não Funcionais da Contratação",
            ),
            ft.TextField(
                label="Memória de Cálculo da Contratação, quantidade e valor",
                multiline=True,
                helper_text="Descreva a memória de cálculo da contratação, com seus valores e quantidades",
            ),
            ft.TextField(
                label="Contratações anteriores",
                multiline=True,
                helper_text="Descreva as contratações anterires, no seguinte formato (<nome>...<nome/> <valores>...<valores>)",
            ),
            ft.TextField(
                label="Levantamento de contratações públicas",
                multiline=True,
                helper_text="Descreva as contratações levantadas na seguinte forma: (<descrição>...<descrição/> <valor>...<valor/>)",
            ),
            ft.TextField(
                label="Soluções de Mercado",
                multiline=True,
                helper_text="Soluções de mercado: (<descrição>...<descrição/> <adequação>...<adequação/> <melhor solução>...<melhor solução/> <justificativa>...<justificativa/>)",
            ),
            ft.TextField(
                label="Justificativa de Parcelamento do Objeto",
                multiline=True,
                helper_text="Coloque a justificativa do parcelamento"
            ),
            ft.TextField(label="Justificativa de economicidade", multiline=True),
            ft.TextField(
                label="Impactos ambientais",
                multiline=True,
                helper_text="Descreva os impactos ambientais da contratação",
            ),
            ft.TextField(
                label="Gestão de Risco",
                multiline=True,
                helper_text="Descreva a gestão de risco: (<risco>...<risco/> <probabilidade>...<probabilidade/> <impacto>...<impacto/> <mitigação>...<mitigação/>)",
            ),
        ]
        submit = ft.ElevatedButton("Enviar", on_click=self.enviar_projeto)
        cancel = ft.ElevatedButton("Cancelar", on_click=self.cancelar_projeto)
        formulario = ft.Column(controls=[*self.form, ft.Row(controls=[submit, cancel])], scroll=ft.ScrollMode.AUTO, spacing=15)
        return formulario

    def build_anteriores(self):
        with Session(self.engine) as session:
            statement = select(ETP)
            result = session.exec(statement=statement).all()
        
        def card(result):
            lv = ft.ListView(spacing=10, padding=20, auto_scroll=True)
            for r in result:
                lv.controls.append(ft.ListTile(
                        leading=ft.Icon(ft.Icons.ALBUM),
                        title=ft.Text(f"Projeto -> {r.nome_do_projeto}"),
                        trailing=ft.TextButton(
                                "Acessar",
                                on_click=self.mostrar_resultado,
                                data=r.id_
                            )
                    ))
            return lv

        return ft.Column(controls=[card(result=result)])

    def mostrar_resultado(self, event):
        print(event.control.data)
        event.page.session.set("id_etp", event.control.data)
        event.page.route = "/resultado"
        event.page.go(event.page.route)
