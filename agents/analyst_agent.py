from crewai import Agent
from config.llm_config import local_llm
from tools.akshare_tools import get_stock_data


analyst_agent = Agent(
    role="量化分析师",

    goal="""
    获取真实股票历史数据，
    分析股价趋势与成交量变化。
    """,

    backstory="""
    你精通A股技术分析。
    你必须基于真实数据判断：
    上涨、下跌、震荡。
    """,

    llm=local_llm,

    tools=[get_stock_data],

    verbose=True
)