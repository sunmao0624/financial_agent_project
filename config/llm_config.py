import os

from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaEmbeddings
from crewai import LLM

os.environ["OPENAI_API_KEY"] = "sk-9313d9bc97fd4d9e95348b841eb7f7fc"
os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"

# # 使用 OpenAI 兼容模式调用本地 Ollama，彻底避开原生协议的 Empty Bug
# local_llm = ChatOpenAI(
#     model="ollama/qwen3.5:4b",  # 明确告诉 litellm 走 ollama 协议
#     base_url="http://localhost:11434/v1",
#     temperature=0.1,
#     max_retries=3,    # 如果偶尔响应空，允许框架在底层自动重试 3 次
#     timeout=300,
#     max_tokens=4096,  # 增加最大生成长度，确保长篇研报能写完
#     model_kwargs={
#         "extra_body": {
#             "num_ctx": 8192  # 强制 Ollama 将上下文窗口扩大到 8K，防止前面 Agent 的输出把窗口撑爆
#         }
#     }
# )

# 使用 OpenAI deepseek api调用形式
local_llm = ChatOpenAI(
    model="openai/deepseek-v4-pro",
    temperature=0.1,
    max_retries=3,
    timeout=300,
    max_tokens=8192
)

# 3. 知识库向量模型 (Embeddings)
local_embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

print("DeepSeek LLM 初始化成功！")