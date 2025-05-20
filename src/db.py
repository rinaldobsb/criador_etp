# from typing import List
# from decimal import Decimal
from sqlmodel import (SQLModel, 
                      Field, 
                    #   Relationship, 
                      create_engine)


def create_database(database):
    sqlite_file_name = f"{database}.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)
    return engine


def connect_database(database):
    sqlite_file_name = f"{database}.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    return create_engine(sqlite_url, echo=True)


class ETP(SQLModel, table=True):
    id_: int = Field(primary_key=True) # foi alterado TODO: alterar nos outros lugares, não pode iniciar com underscore
    nome_do_projeto: str | None = Field(title="Nome do Projeto")
    # objetivo: str | None = Field(title="Objetivo do Documento ETP")
    # lista_objetos: List["List_Objetos_ETP"] = Relationship(back_populates="etp")
    # lista_problemas: List["List_Problemas_ETP"] = Relationship(back_populates="etp")
    # lista_necessidades: List["List_Necessidades_ETP"] = Relationship(
    #     back_populates="etp"
    # )
    # Lista_beneficios: List["List_Beneficios_ETP"] = Relationship(back_populates="etp")
    # lista_alinhamentos: List["List_Alinhamentos_ETP"] = Relationship(
    #     back_populates="etp"
    # )
    # lista_requisitos: List["List_Requisitos_ETP"] = Relationship(back_populates="etp")
    # lista_quantidade_e_calculo: List["List_Memorias_Calculos_ETP"] = Relationship(
    #     back_populates="etp"
    # )
    # lista_contratacoes_anteriores: List["List_Contratacoes_Anteriores_ETP"] = (
    #     Relationship(back_populates="etp")
    # )
    # lista_contratacoes_publicas: List["List_Contratacoes_Publicas_ETP"] = Relationship(
    #     back_populates="etp"
    # )
    # lista_solucoes_de_mercado: List["List_Solucoes_de_Mercado_ETP"] = Relationship(
    #     back_populates="etp"
    # )
    # justificativa_parcelamento: str | None = Field(
    #     title="Justificativa de parcelamento da contratação"
    # )
    # justificativa_de_economicidade: str | None = Field(
    #     title="Justificativa de benefícios econômicos."
    # )
    # impactos_ambientais: str | None = Field(
    #     title="Descrição de impactos ambientais, caso exista"
    # )
    # risk_management: List["List_Risco_ETP"] = Field(
    #     title="Gestão de Risco",
    #     description="Lista de riscos da contratação, com a probabilidade de ocorrer, o impacto e as ações de mitigação.",
    # )
    # preco_total: Decimal = Field(title="Preço total dos bens ou dos serviços")
    text_markdown: str = Field(title="ETP em formato Markdown")


# class List_Objetos_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_objeto: int | None = Field(foreign_key="objeto._id")
#     objetos: List["Objeto_ETP"] = Relationship(back_populates="lista")
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="lista_objetos")


# class Objeto_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     name: str = Field(title="Nome do item para a contratação")
#     description = Field(title="Descrição do item")
#     quant: int = Field(title="Quantidade do item")
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Objetos_ETP | None = Relationship(back_populates="objetos")


# class List_Problemas_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_problema: int | None = Field(foreign_key="problema._id")
#     problemas: List["Problema_ETP"] = Relationship(back_populates="lista")
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="lista_problemas")


# class Problema_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     problema: str | None = Field(title="Problema a ser resolvido com a contratação")
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Problemas_ETP | None = Relationship(back_populates="problemas")


# class List_Necessidades_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_necessidade: int | None = Field(foreign_key="necessidade._id")
#     necessidades: List["Necessidade_ETP"] = Relationship(back_populates="lista")
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="lista_necessidades")


# class Necessidade_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     necessidade: str | None = Field(
#         title="Necessidade a ser resolvida com a contratação"
#     )
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Necessidades_ETP | None = Relationship(back_populates="necessidades")


# class List_Beneficios_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_beneficio: int | None = Field(foreign_key="beneficio._id")
#     beneficios: List["Beneficio_ETP"] = Relationship(back_populates="lista")
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="lista_beneficios")


# class Beneficio_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     beneficio: str | None = Field(title="Benefício alcançado com a contratação")
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Beneficios_ETP | None = Relationship(back_populates="beneficios")


# class List_Alinhamentos_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_alinhamento: int | None = Field(foreign_key="lista._id")
#     alinhamentos: List["Alinhamento_ETP"] = Relationship(back_populates="lista")
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="lista_alinhamentos")


# class Alinhamento_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     normativo: str | None = Field(title="Normativo para alinhamento")
#     relacao: str | None = Field(title="Relação da contratação aos normativos")
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Alinhamentos_ETP | None = Relationship(back_populates="beneficios")


# class List_Requisitos_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_requisito: int | None = Field(foreign_key="lista._id")
#     requisitos: List["Requisito_ETP"] = Relationship(back_populates="lista")
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="lista_requisitos")


# class Requisito_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     requisito: str | None = Field(title="Requisito do Contratação")
#     e_funcional: bool | None = Field(
#         title="Classificação do requisito, se funcional ou não"
#     )
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Requisitos_ETP | None = Relationship(back_populates="requisitos")


# class List_Memorias_Calculos_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_memorias_calculos: int | None = Field(foreign_key="lista._id")
#     memorias_calculos: List["Memoria_Calculo_ETP"] = Relationship(
#         back_populates="lista"
#     )
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="lista_memorias_calculos")


# class Memoria_Calculo_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     item: str | None = Field(title="Item da Contratação")
#     calculo: str | None = Field(title="Cálculo do item da contratação")
#     quantidade: int | None = Field(title="Quantidade do item")
#     total: Decimal | None = Field(title="Valor total do item", decimal_places=2)
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Memorias_Calculos_ETP | None = Relationship(
#         back_populates="memorias_calculos"
#     )


# class List_Contratacoes_Anteriores_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_contratacoes_anteriores: int | None = Field(foreign_key="lista._id")
#     contratacoes_anteriores: List["Contratacao_Anterior_ETP"] = Relationship(
#         back_populates="lista"
#     )
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="lista_contratacoes_anteriores")


# class Contratacao_Anterior_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     descricao: str | None = Field(title="Descrição da contratação anterior")
#     valor_total: Decimal | None = Field(
#         title="Total da contratação anterrior", decimal_places=2
#     )
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Contratacoes_Anteriores_ETP | None = Relationship(
#         back_populates="contratacoes_anteriores"
#     )


# class List_Contratacoes_Publicas_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_contratacoes_publicas: int | None = Field(foreign_key="lista._id")
#     contratacoes_publicas: List["Contratacao_Publica_ETP"] = Relationship(
#         back_populates="lista"
#     )
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="lista_contratacoes_publicass")


# class Contratacao_Publica_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     descricao: str | None = Field(title="Nome da Contratação Pública")
#     orgao: str | None = Field(title="Órgão que fez a contratação")
#     valor_total: Decimal | None = Field(
#         title="Valor total da contratação", decimal_places=2
#     )
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Contratacoes_Publicas_ETP | None = Relationship(
#         back_populates="contratacoes_publicas"
#     )


# class List_Solucoes_de_Mercado_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_solucoes_de_mercado: int | None = Field(foreign_key="lista._id")
#     solucoes_de_mercado: List["Solucao_de_Mercado_ETP"] = Relationship(
#         back_populates="lista"
#     )
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="lista_solucoes_de_mercado")


# class Solucao_de_Mercado_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     descricao: str = Field(title="Descrição da solução de mercado")
#     adequada: bool = Field(title="É ou não é adequada para a contratação")
#     justificativa: str = Field(
#         title="Descrição se é adequada ou não para a contratação"
#     )
#     motivo_para_escolha: str = Field(title="Se adequada, descreve o motivo da escolha")
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Solucoes_de_Mercado_ETP | None = Relationship(
#         back_populates="solucoes_de_mercado"
#     )


# class List_Risco_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     id_risco: int | None = Field(foreign_key="lista._id")
#     riscos: List["Risco_ETP"] = Relationship(back_populates="lista")
#     etp_id: int | None = Field(default=None, foreign_key="etp._id")
#     etp: ETP | None = Relationship(back_populates="risk_management")


# class Risco_ETP(SQLModel, table=True):
#     _id: int | None = Field(default=None, primary_key=True)
#     descricao: str = Field(title="Descrição do Risco da contratação")
#     probabilidade: float = Field(
#         title="Probabilidade do Risco ocorrer, entre 0% e 100%", ge=0.0, le=100.0
#     )
#     impacto: float = Field(
#         title="Impacto da ocorrência do risco no órgão, com medição entre 0% e 100%",
#         ge=0.0,
#         le=100.0,
#     )
#     mitigacao: str = Field(title="Ação de mitigação")
#     lista_id: int | None = Field(default=None, foreign_key="lista._id")
#     lista: List_Risco_ETP | None = Relationship(back_populates="riscos")


class Users(SQLModel, table=True):
    id_: int | None = Field(default=None, primary_key=True)
    user: str = Field(unique=True)
    password: str
