from crewai import Task
from agents.chart_agent import chart_agent

def create_chart_task(symbol):
    return Task(
        description=f"""
        为股票 {symbol} 生成一张专业的技术分析图表。
        必须调用 `generate_professional_chart` 工具。
        提取工具返回的 Markdown 图片链接作为最终输出。
        """,
        expected_output="一段包含本地图片路径的 Markdown 语法字符串，例如：![图表](output/xxx.png)",
        agent=chart_agent
    )