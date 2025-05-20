from agno.vectordb.lancedb import LanceDb
from agno.vectordb.search import SearchType
from agno.embedder.google import GeminiEmbedder

# LanceDB Vector DB
def my_vector_db1(configurations, path):
    return LanceDb(
    table_name="conhecimentos_etp",
    uri=path,
    search_type=SearchType.hybrid,
    embedder=GeminiEmbedder(
        api_key=configurations("src/.env.toml").get("GEMINI_API")
    )
)

def my_vector_db2(configurations, path):
    return LanceDb(
    table_name="conhecimentos_leis",
    uri=path,
    search_type=SearchType.hybrid,
    embedder=GeminiEmbedder(
        api_key=configurations("src/.env.toml").get("GEMINI_API")
    )
)

def my_vector_db_combined(configurations, path):
    return LanceDb(
    table_name="conhecimentos_combined",
    uri=path,
    search_type=SearchType.hybrid,
    embedder=GeminiEmbedder(
        api_key=configurations("src/.env.toml").get("GEMINI_API")
    )
)