# agente
from typing import List

from etp import ETP_Document
from db import ETP, connect_database
from template import template
from configs import configurations
from bases_de_conhecimento import base_conhecimento
from tools import baidu, duckduckgo, jreader, thinking_tool

from sqlmodel import Session, insert

from agno.agent import Agent
from agno.models.google import Gemini
from agno.team.team import Team


searcher_agent = Agent(
    model=Gemini(
        id="gemini-2.5-flash", api_key=configurations(".env.toml").get("GEMINI_API")
    ),
    name="Agente de Pesquisa na Internet na área de Licitações e Contratos Administrativos",
    description="Você é um especialsita em pesquisas na web na área de Licitações e Contratos Administrativos e Tecnologia em geral. \
        Você pode encontrar qualquer artigo, postagem, publicação e site na área de Licitações e Contratos e tecnologias em geral.",
    role="Seu papel é pesquisar na internet tudo o que for necessário para a elaboração do Estudo Técnico Preliminar",
    instructions=[
        "Recebida as informações de entrada, você irá elaborar um plano de pesquisa",
        "Você irá pesquisar tudo o que for necessário para subsidiar as elaboração do ETP, seguindo este plano de pesquisa.",
        "Você começará pesquisando em sites governamentais do Brasil acerca dos temas de Licitações e Contratos e Tecnologia, \
            tais como o site do Planalto, o Portal do PNCP e o portal do TCU",
        "Depois você pesquisará em sites como Zênite, Âmbito Jurídico, Senado Federal, Enap, IPOG, Projuris, Acadêmico, IBEGESP, Portal L&C, Direito Net, CGU e Justen",
        "Depois você pesquisará, também, nos demais sites, quando for necessário.",
        "Raciocine sobre o que é importante para a pesquisa e exponha as conclusões que sejam úteis para a elaboração do ETP."
    ],
    tools=[baidu, duckduckgo, jreader, thinking_tool],
    add_datetime_to_instructions=True
)

knowledge_agent = Agent(
    model=Gemini(
        id="gemini-2.5-flash", api_key=configurations(".env.toml").get("GEMINI_API")
    ),
    name="Agente de Conhecimento especialista em Licitações e Contratos",
    description="Você é um agente de conhecimento, especilista em Licitações e Contratos, que tem acesso às bases de conhecimento do órgãos para subsidiar a elaboração \
        do Estudo Técnico Preliminar.",
    role="Seu papel é pesquisar na base de conhecimento e trazer elementos necessários para a elaboração do ETP.",
    instructions=[
        "Recebida os dados de entrada, você irá consultar a base de conhecimento",
        "Você sistematizará a consulta e trará os dados necessários para a elaboração do ETP"
    ],
    knowledge=base_conhecimento,
    search_knowledge=True
)

technologist_agent = Agent(
    model=Gemini(
        id="gemini-2.5-flash", api_key=configurations(".env.toml").get("GEMINI_API")
    ),
    name="Agente de Conhecimento especialista em Tecnologia da Informação",
    description="Você é um especialsita em pesquisas na web na área de Tecnologia da Informação. \
        Você pode encontrar qualquer artigo, postagem, publicação e site na área de Tecnologia da Informação",
    role="Seu papel é pesquisar na internet tudo o que for necessário para a elaboração do Estudo Técnico Preliminar",
    instructions=[
        "Recebida as informações de entrada, você irá pesquisar o que for necessário para subsidiar as elaboração do ETP",
        "Você começará pesquisando em sites técnicos de tecnologia da informação e sites de empresas relacionadas.",
        "Você também pesquisará em documentações técnicas e artigos técnicos de Tecnologia da Informação.",
        "Raciocine sobre o que é necessário e exponha as conclusões que sejam úteis para a elaboração do ETP"
    ],
    tools=[baidu, duckduckgo, jreader, thinking_tool],
    add_datetime_to_instructions=True
)

assistant_elaboration_agent = Agent(
    model=Gemini(
        id="gemini-2.5-flash", api_key=configurations(".env.toml").get("GEMINI_API")
    ),
    name="Assistente do Editor do Estudo Técnico Preliminar",
    description="Você é um assistente do Editor de Estudo Técnico Preliminar, e seu objetivo é auxiliar na elaboraração do ETP, \
        produzindo uma saída estruturada das informações necessárias para a edição do ETP.",
    instructions=[
        "Você receberá os dados de entrada, e prduizirá uma saída estruturada da informações.",
        "Você seguirá o plano do Editor passo a passo.",
    ],
    response_model=ETP_Document,
    use_json_mode=True
)

editor_do_ETP = Team(
    model=Gemini(
        id="gemini-2.5-flash", api_key=configurations(".env.toml").get("GEMINI_API")
    ),
    name="Editor de Estudo Técnico Preliminar especializado.",
    mode="coordinate",
    members=[searcher_agent, knowledge_agent, technologist_agent, assistant_elaboration_agent],
    description="Você é um editor de Estudo Técnico Preliminar nível Senior, e seu objetivo é elaborar, com as informações recebidas, \
        o Estudo Técnico Preliminar, com todos ou a maior parte dos elementos necessários para a edição.",
    instructions=[
        "Você receberá os dados de entrada, e elaborará um plano para realizar a escrita do ETP.",
        "Você seguirá o plano passo a passo.",
        "Você poderá delegar para os demais agentes o que for necessário para a elaboração do ETP.",
        "Você irá colher os dados dos demais agentes e verificará o que for mais pertinente para a elaboração do ETP.",
        "Lembre-se: o ETP deverá ter as seções e parágrafos numerados progressivamente e de maneira clara, com base em estrutura semelhante \
            da Resolução CNJ 468 de 2022, e das estruturas dos ETPs da base de conhecimento."
    ],
    reasoning=True,
    reasoning_min_steps=3,
    add_datetime_to_instructions=True,
    add_member_tools_to_system_message=False,
    enable_agentic_context=True,
    share_member_interactions=True,
    markdown=True,
    expected_output=template

)
    
def processa_dados(lista_dados: List):
    nome_projeto = lista_dados.pop(0)
    output_data: str = ""
    for d in lista_dados:
        output_data += d + " \n\n"
    return nome_projeto, output_data

def recebe_dados(dados: List) -> int:
    nome_projeto, input = processa_dados(dados)
    resultado = editor_do_ETP.run(message=input)
    dados_para_inserir = ETP(nome_do_projeto=nome_projeto, text_markdown=resultado)
    with Session(connect_database("database")) as session:
        session.add(dados_para_inserir)
        session.commit()
    return resultado




