from agno.tools.baidusearch import BaiduSearchTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.jina import JinaReaderTools
from agno.tools.reasoning import ReasoningTools

from configs import configurations


header = """User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35"""
header2 = "User_Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35"

baidu = BaiduSearchTools(fixed_language="pt-BR", fixed_max_results=25)

duckduckgo = DuckDuckGoTools(fixed_max_results=25)

jreader = JinaReaderTools(api_key=configurations("src/.env.toml").get("JINAREADER"), max_content_length=8000)

thinking_tool = ReasoningTools(add_instructions=True, instructions="Pensar em tópicos bem explicados para a construção do plano de pesquisa na internet.")