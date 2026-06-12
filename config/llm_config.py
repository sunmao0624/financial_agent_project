from langchain_openai import ChatOpenAI
from langchain_community.embeddings import OllamaEmbeddings


local_llm = ChatOpenAI(
    model="qwen3.5",
    api_key="ollama",
    base_url="http://localhost:11434/v1",
    temperature=0
)

local_embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

print("LLM 初始化成功")