from agno.knowledge.text import TextKnowledgeBase
from agno.knowledge.combined import CombinedKnowledgeBase
from vectordb import my_vector_db1, my_vector_db2, my_vector_db_combined
from main import my_path

base_de_etps = TextKnowledgeBase(
    path=my_path / "base_de_conhecimento" / "base_de_conhecimento_etps",
    vector_db=my_vector_db1,
    num_documents=10,
    formats=[".txt", ".md"]
)
base_de_leis = TextKnowledgeBase(
    path=my_path / "base_de_conhecimento" / "base_de_conhecimento_leis",
    vector_db=my_vector_db2,
    num_documents=10,
    formats=[".txt", ".md"]
)

base_conhecimento = CombinedKnowledgeBase(
    sources=[base_de_etps, base_de_leis],
    vector_db=my_vector_db_combined,
    num_documents=10
)
