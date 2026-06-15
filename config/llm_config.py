import os

from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaEmbeddings
from crewai import LLM

os.environ["OPENAI_API_KEY"] = "ollama"

# 使用 OpenAI 兼容模式调用本地 Ollama，彻底避开原生协议的 Empty Bug
local_llm = ChatOpenAI(
    model="ollama/qwen3.5:4b",  # 明确告诉 litellm 走 ollama 协议
    base_url="http://localhost:11434/v1",
    temperature=0.1,
    max_retries=3,    # 如果偶尔响应空，允许框架在底层自动重试 3 次
    timeout=300,
    # max_tokens=2048  # 增加最大生成长度，确保长篇研报能写完
)

local_embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

print("LLM 初始化成功")