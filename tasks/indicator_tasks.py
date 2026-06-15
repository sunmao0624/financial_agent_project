from crewai import Task
from agents.indicator_agent import indicator_agent


def create_indicator_task(symbol):

    return Task(

        description=f"""
        使用工具 calculate_indicators 计算股票 {symbol} 技术指标。

        必须执行：

        1. 调用 calculate_indicators 工具

        2. 获取技术指标结果

        3. 保留工具返回的 JSON 数据

        4. 不允许修改 JSON 格式

        5. 不允许只输出文字结论

        必须原样返回工具结果。
        """,

        expected_output="JSON格式技术指标数据",

        agent=indicator_agent
    )