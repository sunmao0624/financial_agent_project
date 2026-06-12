from crewai import Agent
from config.llm_config import local_llm


risk_agent = Agent(
    role="风险控制分析师",

    goal="""
    判断短期风险。
    """,

    backstory="""
    你负责判断：

    是否超买

    是否存在回撤

    波动是否异常
    """,

    llm=local_llm,

    verbose=True
)