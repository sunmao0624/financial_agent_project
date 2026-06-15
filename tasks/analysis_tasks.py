from crewai import Task
from agents.analyst_agent import analyst_agent


def create_analysis_task(symbol):
    return Task(
        description=f"""
        使用工具 get_stock_data 获取股票 {symbol} 最近30日数据。
        必须：
        1. 提取最近30日收盘价列表
        2. 提取最近30日成交量列表
        3. 保留 JSON 原始数据
        4. 不允许修改工具返回格式
        必须原样返回。
        """,
        expected_output="结构化股票数据分析",
        agent=analyst_agent
    )