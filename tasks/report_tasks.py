from crewai import Task
from agents.writer_agent import writer_agent


def create_report_task(
        analysis_task,
        indicator_task,
        risk_task,
        chart_task
):

    return Task(
        description="""
                综合所有 Agent 输出生成金融研报。
                输入包括：
                1. 走势分析结果
                2. 技术指标结果
                3. 风险评估结果
                4. 图表 Agent 输出
                必须遵守：
                如果输入中存在：
                ![xxx](xxx.png)
                必须原样复制。
                禁止修改图片路径。
                禁止删除 Markdown 图片语法。
                禁止用文字替代图片。
                输出结构：
                # 标题
                ## 图表展示
                (直接粘贴 Markdown 图片)
                ## 走势分析
                ## 技术指标
                ## 风险分析
                ## 投资建议
                """,
        expected_output="完整 Markdown 投资研究报告",

        agent=writer_agent,

        context=[
            analysis_task,
            indicator_task,
            risk_task,
            chart_task
        ]
    )