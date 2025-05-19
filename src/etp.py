from typing import List
from decimal import Decimal

from pydantic import BaseModel, Field
from dados import exemplos_de_objetivos, exemplos_de_problemas


class Objeto_ETP(BaseModel):
    """Representa um item da contratação com nome, descrição e quantidade"""

    name: str = Field(title="Nome do item para a contratação")
    description: str = Field(title="Descrição do item")
    quant: int = Field(title="Quantidade do item")


class Alinhamento_ETP(BaseModel):
    """Representa um alinhamento da contratação"""

    normativo: str = Field(title="Normativo")
    relacao: str = Field(title="Relação entre o normativo e a contratação")


class Requisitos_ETP(BaseModel):
    """Representa uma lista de requisitos da contratação"""

    requisitos: List[str] = Field(
        title="Lista de requistos funcionais para a contratação"
    )
    e_funcional: bool = Field(title="Define se é requisito funcional ou não funcional")


class Memoria_Calculo_ETP(BaseModel):
    """Representa a memória de Cálculo de um item da contratação"""

    item: str = Field(title="Item da Contratação")
    calculo: str = Field(title="Memória de Cálculo do item")
    quantidade: int = Field(title="Quantidade do item")
    total: Decimal = Field(title="Valor total do item", decimal_places=2)


class Contratacao_Anterior_ETP(BaseModel):
    """Representa uma contratação anterior, que é pertinente à atual"""

    descricao: str = Field(title="Descrição da contratação anterior")
    valor_total: Decimal = Field(
        title="Total da contratação anterrior", decimal_places=2
    )


class Contratacoes_Publicas_ETP(BaseModel):
    """Representa uma contratação pública de outro órgão que se relaciona à contratação em comento"""

    descricao: str = Field(title="Nome da Contratação Pública")
    orgao: str = Field(title="Órgão que fez a contratação")
    valor_total: Decimal = Field(title="Valor total da contratação", decimal_places=2)


class Solucoes_de_Mercado_ETP(BaseModel):
    """Representa uma solução de mercado que é referida à contratação em comento"""

    descricao: str = Field(title="Descrição da solução de mercado")
    adequada: bool = Field(title="É ou não é adequada para a contratação")
    justificativa: str = Field(
        title="Descrição se é adequada ou não para a contratação"
    )
    motivo_para_escolha: str = Field(title="Se adequada, descreve o motivo da escolha")


class Risco_ETP(BaseModel):
    """Representa um risco da contratação"""

    descricao: str = Field(title="Descrição do Risco da contratação")
    probabilidade: float = Field(
        title="Probabilidade do Risco ocorrer, entre 0% e 100%", ge=0.0, le=100.0
    )
    impacto: float = Field(
        title="Impacto da ocorrência do risco no órgão, com medição entre 0% e 100%",
        ge=0.0,
        le=100.0,
    )
    mitigacao: str = Field(title="Ação de mitigação")


class ETP_Document(BaseModel):
    """Representa o documento ETP que será construído para a contratação em comento"""

    nome_do_projeto: str = Field(title="Nome do Projeto")
    objetivo: str = Field(
        title="Objetivo do Documento ETP",
        description="Descrição do objetivo do Documento, que é uma contratação de bens ou de serviços",
        examples=exemplos_de_objetivos,
    )
    objetos: List[Objeto_ETP] = Field(
        title="Lista de itens para contratação",
        description="Itens da Contratação, com nome do item, descrição e quantidade.",
    )
    problemas: List[str] = Field(
        title="Problemas a serem resolvidos",
        description="Lista de descrição dos problemas a serem resolvidos",
        examples=exemplos_de_problemas,
    )
    necessidades: List[str] = Field(
        title="Necessidade de contratar",
        description="Lista de necessidades para se contratar bens ou serviços para resolver os problemas",
    )
    beneficios_diretos: List[str] = Field(
        title="Benefícios Diretos da Contratação",
        description="Lista dos benefícios diretos da contratação dos bens ou serviços do objetivo.",
    )
    beneficios_indiretos: List[str] = Field(
        title="Benefícios Indiretos da Contratação",
        description="Lista dos benefícios indiretos da contratação dos bens ou serviços do objetivo.",
    )
    alinhamento: List[Alinhamento_ETP] = Field(
        title="Alinhamento com a Resolução do CNJ e Plano Diretor do Tribunal",
        description="Descreve a relação e como se alinha com a Resolução do CNJ e com o Plano Diretor do TRE-DF",
    )
    requisitos: List[Requisitos_ETP] = Field(
        title="Descrição dos Requsitos Funcionais e Não Funcionais",
        description="Lista de requisitos funcionais e não funcionais dos bens ou serviços que se quer contratar",
    )
    quantidade_e_calculo: List[Memoria_Calculo_ETP] = Field(
        title="Lista de bens e serviços com suas quantidades, cálculos e total",
        description="Lista dbens ou serviços, com suas quantidades, memória de cálculo e totais",
    )
    contratacoes_anteriores: List[Contratacao_Anterior_ETP] = Field(
        title="Lista de contratações anteriores",
        description="Lista de contrataçõea anteriores",
    )
    contratacoes_publicas: List[Contratacoes_Publicas_ETP] = Field(
        title="Lista de outras contratações Públicas",
        description="Lista com outras contratações públicas semelhantes",
    )
    levantamentos: List[Solucoes_de_Mercado_ETP] = Field(
        title="Soluções de mercado",
        description="Lista de soluções de mercado pesquisadas e sua adequação à contratação",
    )
    justificativa_parcelamento: str = Field(
        title="Justificativa de parcelamento da contratação",
        description="Justificativa de parcelamento da Contratação, segundo a Lei de Licitações e Contratos, Lei 14133",
    )
    justificativa_de_economicidade: str = Field(
        title="Justificativa de benefícios econômicos.",
        description="Elencar os benefícios diretos e indiretos que o órgão almeja com a contratação, em termos de economicidade, eficácia, eficiência, de melhor aproveitamento dos recursos humanos, materiais e financeiros disponíveis, inclusive com respeito a impactos ambientais positivos e melhoria da qualidade de produtos ou serviços oferecidos à sociedade",
    )
    impactos_ambientais: str = Field(
        title="Descrição de impactos ambientais, caso exista",
        description="Descrição dos impactos ambientais da contratação, caso exita",
    )
    risk_management: List[Risco_ETP] = Field(
        title="Gestão de Risco",
        description="Lista de riscos da contratação, com a probabilidade de ocorrer, o impacto e as ações de mitigação.",
    )
    preco_total: Decimal = Field(title="Preço total dos bens ou dos serviços")
