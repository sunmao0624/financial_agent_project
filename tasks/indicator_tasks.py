from crewai import Task
from agents.indicator_agent import indicator_agent


def create_indicator_task(symbol):

    return Task(
        description=f"""
        计算股票 {symbol}

        MA5

        MA10

        RSI
        """,

        expected_output="技术指标",

        agent=indicator_agent
    )