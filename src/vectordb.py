from agno.vectordb.lancedb import LanceDb
from agno.vectordb.search import SearchType
from agno.embedder.google import GeminiEmbedder
from configs import configurations
from main import my_path

# LanceDB Vector DB
my_vector_db1 = LanceDb(
    table_name="conhecimentos_etp",
    uri=my_path / "vector_db",
    search_type=SearchType.hybrid,
    embedder=GeminiEmbedder(
        api_key=configurations(".env.toml").get("GEMINI_API")
    )
)

my_vector_db2 = LanceDb(
    table_name="conhecimentos_leis",
    uri=my_path / "vector_db",
    search_type=SearchType.hybrid,
    embedder=GeminiEmbedder(
        api_key=configurations(".env.toml").get("GEMINI_API")
    )
)

my_vector_db_combined = LanceDb(
    table_name="conhecimentos_combined",
    uri=my_path / "vector_db",
    search_type=SearchType.hybrid,
    embedder=GeminiEmbedder(
        api_key=configurations(".env.toml").get("GEMINI_API")
    )
)