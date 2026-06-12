from crewai import Crew
from crewai import Process

from tasks.analysis_tasks import create_analysis_task
from tasks.indicator_tasks import create_indicator_task
from tasks.risk_tasks import create_risk_task
from tasks.report_tasks import create_report_task

from agents.analyst_agent import analyst_agent
from agents.indicator_agent import indicator_agent
from agents.risk_agent import risk_agent
from agents.writer_agent import writer_agent


def run(symbol):

    crew = Crew(
        agents=[
            analyst_agent,
            indicator_agent,
            risk_agent,
            writer_agent
        ],

        tasks=[
            create_analysis_task(symbol),
            create_indicator_task(symbol),
            create_risk_task(),
            create_report_task()
        ],

        process=Process.sequential
    )

    result = crew.kickoff()

    print(result)


if __name__ == "__main__":
    run("002459")