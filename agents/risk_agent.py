from crewai import Agent
from config.llm_config import local_llm

from tools.risk_tools import (
    calculate_max_drawdown,
    calculate_volatility
)
risk_agent = Agent(
    role="风险控制分析师",
    goal="""
    识别股票短期风险。
    """,
    backstory="""
    你是专业量化风控分析师。
    你需要：
    判断超买状态
    计算最大回撤
    计算波动率
    判断短期风险等级
    """,
    tools=[
        calculate_max_drawdown,
        calculate_volatility
    ],
    llm=local_llm,
    verbose=True
)