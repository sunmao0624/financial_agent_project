from crewai import Task
from agents.risk_agent import risk_agent


def create_risk_task(symbol):

    return Task(
        description=f"""
        分析股票 {symbol} 风险。
        必须：
        1. 使用 calculate_max_drawdown 工具
        2. 使用 calculate_volatility 工具
        3. 根据技术指标判断：
           是否超买
        4. 判断：
           低风险 / 中风险 / 高风险
        输出详细风险报告
        """,
        expected_output="完整风险评估",
        agent=risk_agent
    )