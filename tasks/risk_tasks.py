from crewai import Task
from agents.risk_agent import risk_agent


def create_risk_task():

    return Task(
        description="""
        根据前面结果判断：

        1. 风险等级

        2. 是否超买

        3. 是否存在回撤
        """,

        expected_output="风险评估",

        agent=risk_agent
    )