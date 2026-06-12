from crewai import Task
from agents.analyst_agent import analyst_agent


def create_analysis_task(symbol):

    return Task(
        description=f"""
        获取股票 {symbol} 最近30日行情。

        分析：

        1. 趋势

        2. 成交量变化

        3. 总结走势
        """,

        expected_output="股票趋势分析",

        agent=analyst_agent
    )