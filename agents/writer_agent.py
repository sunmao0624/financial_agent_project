from crewai import Agent
from config.llm_config import local_llm


writer_agent = Agent(
    role="证券研究员",

    goal="""
    根据多个分析师结果生成专业投研报告。
    """,

    backstory="""
    你曾任职券商研究所。

    输出必须专业。

    Markdown格式。
    """,

    llm=local_llm,

    verbose=True
)