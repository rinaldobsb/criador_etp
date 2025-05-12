import json
from textwrap import dedent
from typing import Dict, Iterator, Optional, List, Tuple

from .dados import exemplos_de_objetivos, exemplos_de_problemas
from .configs import configurations


from agno.agent import Agent
from agno.models.google import Gemini
from agno.workflow import Workflow, RunEvent, RunResponse
from agno.storage.sqlite import SqliteStorage
from agno.utils.log import logger

from pydantic import BaseModel, Field


class ETP_Document(BaseModel):
    title: str
    objetivo: str = Field(title="Objetivo do Documento ETP", description="Descrição do objetivo do Documento, que é uma contratação de um bem ou de um serviço", examples=exemplos_de_objetivos)
    problema: str = Field(title="Problemas a serem resolvidos", description="Descrição dos problemas a serem resolvidos", examples=exemplos_de_problemas)
    necessidade: str = Field(title="Necessidade de contratar", description="Descreve a necessidade de contratar o bem ou serviço para resolver o problema")
    beneficios: str = Field(title="Benefícios da Contratação", description="Descrição dos benefícios da contratação dos bens ouserviços do objetivo. elencar benefícios diretos e indiretos.")
    alinhamento: str = Field(title="Alinhamento com a Resolução do CNJ e Plano Diretor do Tribunal", description="Descreve a relação e como se alinha com a Resolução do CNJ e com o Plano Diretor do TRE-DF")
    requisitos: str = Field(title="Descrição dos Requsitos Funcionais e Não Funcionais", description="Descreve os requisitos funcionais e não funcionais do bem ou serviço que se quer contratar")
    quantidade_e_calculo: List[Tuple[str, int, str]] = Field(title="Lista de bens e serviços com suas quantidades e cálculos", description="Lista de tuplas com um bem ou serviço e sua quantidade e memória de cálculo")
    contratacoes_anteriores: List[str] = Field(title="Lista de contratações anteriores", description="Lista de contrataçõea anteriores")
    contratacoes_publicas: List[str] = Field(title="Lista de outras contratações Públicas", description="Lista com outras contratações públicas semelhantes")
    levantamentos: List[str] = Field(title="Soluções de mercado", description="Lista de soluções de mercado levantadas em uma pesquisa")
    melhor_solução: str = Field(title="Justificativa da melhor solução", description="Descrição da melhor solução dentre as levantadas pelo mercado")
    solucao: str = Field(title="Solução escolhida", description="Descrição da solução de mercado escolhida")
    justificativa_parcelamento: str = Field(title="Justificativa de parcelamento da contratação", description="Justificativa de parcelamento da Contratação, segundo a Lei de Licitações e Contratos, Lei 14133")
    justificativa_de_economicidade: str = Field(title="Justificativa de benefícios econômicos.", description="Elencar os benefícios diretos e indiretos que o órgão almeja com a contratação, em termos de economicidade, eficácia, eficiência, de melhor aproveitamento dos recursos humanos, materiais e financeiros disponíveis, inclusive com respeito a impactos ambientais positivos e melhoria da qualidade de produtos ou serviços oferecidos à sociedade")
    impactos_e_mitigacoes: str = Field(title="Descrição de impactos ambientais e mitigações dos riscos.", description="Descrição dos impactos ambientais e suas mitigaç~eos de risco.")
    precos: str = Field(title="Preços dos produtos ou serviços", description="Preços dos produtos e serviços")


class ETP_Creator(Workflow):
    '''Workflow avançado para a geração dos Estudos Técnicos Preliminares'''
    model = Gemini(id="gemini-2.5-flash", api_key=configurations(".env.toml").get("GEMINI_API"))
    creator_agent = Agent(
        model=self.model,
        name="Agente Criador de ETP",
        description="Você é um especialsita na área de Licitações e Contratos Administrativos. Você irá elaborar um Estudo Técnico Preliminar para as contratações do Tribunal Regional eleitoral do DF (TRE-DF).",
        goal="Seu objetivo é elaborar cada parte do ETP, com base nas informações recebidas do usuário e nas ferramentas disponíveis. Elabore cada parte conforme foi indicado foi indicada.",
        instructions=[
            "Recebida as informações de entrada, você irá elaborar cada parte do ETP, conforme a descrição"
        ],
    )