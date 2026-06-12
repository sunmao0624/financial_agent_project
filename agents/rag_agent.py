from crewai import Agent
from config.llm_config import local_llm
from tools.rag_tools import search_pdf_knowledge


rag_agent = Agent(
    role="知识库检索分析师",

    goal="""
    从历史研报中找到相关行业信息。
    """,

    backstory="""
    你擅长检索券商研报。
    """,

    llm=local_llm,

    tools=[search_pdf_knowledge],

    verbose=True
)