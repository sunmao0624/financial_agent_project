from crewai import Task
from agents.writer_agent import writer_agent


def create_report_task():
    return Task(
        description="""
        综合所有前置Agent的输出写一份金融研报。

        你的输入将包含：
        1. 走势分析结果
        2. 技术指标数据
        3. 风险评估结果
        4. 可视化图表链接 (Markdown格式)

        必须包含以下结构：
        - 标题
        - 图表展示（将收集到的 Markdown 图片链接直接粘贴在这里）
        - 走势回顾
        - 技术指标分析
        - 风险提示
        - 投资建议
        """,
        expected_output="包含数据图表的完整 Markdown 深度投研报告",
        agent=writer_agent
    )