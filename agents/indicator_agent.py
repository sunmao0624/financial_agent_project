from crewai import Agent
from config.llm_config import local_llm
from tools.indicator_tools import calculate_indicators


indicator_agent = Agent(
    role="技术指标分析师",

    goal="""
    根据股票数据计算技术指标。
    """,

    backstory="""
    你擅长:
    MA
    RSI
    MACD
    BOLL
    """,

    llm=local_llm,

    tools=[calculate_indicators],

    verbose=True
)