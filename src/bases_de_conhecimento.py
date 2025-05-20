from agno.knowledge.text import TextKnowledgeBase
from agno.knowledge.combined import CombinedKnowledgeBase


def base_de_etps(path, vector_db):
    return TextKnowledgeBase(
    path=path,
    vector_db=vector_db,
    num_documents=10,
    formats=[".txt", ".md"]
)
def base_de_leis(path, vector_db):
    return TextKnowledgeBase(
    path=path,
    vector_db=vector_db,
    num_documents=10,
    formats=[".txt", ".md"]
)

def base_conhecimento(sources, vector_db):
    return CombinedKnowledgeBase(
    sources=sources,
    vector_db=vector_db,
    num_documents=10
)
