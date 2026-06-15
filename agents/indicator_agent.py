from crewai import Agent
from config.llm_config import local_llm
from tools.indicator_tools import calculate_indicators


indicator_agent = Agent(
    role="技术指标分析师",
    goal="""
    基于股票数据计算技术指标，
    输出结构化 JSON 数据。
    """,
    backstory="""
    你是量化交易员。
    负责计算：
    MA5
    MA10
    RSI
    MACD
    重要要求：
    必须调用工具。
    禁止自己编造数据。
    必须保持 JSON 原始格式。
    结果将交给后续 Agent 使用。
    """,
    llm=local_llm,
    tools=[calculate_indicators],
    verbose=True
)