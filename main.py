from crewai import Crew
from crewai import Process

from tasks.analysis_tasks import create_analysis_task
from tasks.indicator_tasks import create_indicator_task
from tasks.risk_tasks import create_risk_task
from tasks.chart_tasks import create_chart_task  # 新增
from tasks.report_tasks import create_report_task

from agents.analyst_agent import analyst_agent
from agents.indicator_agent import indicator_agent
from agents.risk_agent import risk_agent
from agents.chart_agent import chart_agent  # 新增
from agents.writer_agent import writer_agent


def run(symbol):
    crew = Crew(
        agents=[
            analyst_agent,
            indicator_agent,
            risk_agent,
            chart_agent,  # 新增入列
            writer_agent
        ],
        tasks=[
            create_analysis_task(symbol),
            create_indicator_task(symbol),
            create_risk_task(),
            create_chart_task(symbol),  # 让它在写报告之前生成图表
            create_report_task()
        ],
        process=Process.sequential
    )

    result = crew.kickoff()

    # 将最终研报写到文件里，方便通过支持 Markdown 的编辑器（如 PyCharm 自带的阅读器、Typora、VSCode）查看图片效果
    with open(f"{symbol}_research_report.md", "w", encoding="utf-8") as f:
        f.write(str(result))

    print("===================\n研报已生成并保存为 Markdown 文件！\n===================")


if __name__ == "__main__":
    run("002459")