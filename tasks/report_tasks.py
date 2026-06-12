from crewai import Task
from agents.writer_agent import writer_agent


def create_report_task():

    return Task(
        description="""
        综合所有Agent输出。

        写金融研报。

        包含：

        1. 走势回顾

        2. 技术指标分析

        3. 风险提示

        4. 投资建议
        """,

        expected_output="Markdown报告",

        agent=writer_agent
    )