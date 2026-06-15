import pandas as pd
import ast
from crewai.tools import tool


from crewai.tools import tool
from .data_router import fetch_stock_data_robust


@tool("calculate_max_drawdown")
def calculate_max_drawdown(symbol: str) -> str:
    """
    根据股票代码计算最大回撤
    """

    df = fetch_stock_data_robust(symbol)

    if df.empty:
        return "数据获取失败"

    prices = df["收盘"]

    rolling_max = prices.cummax()

    drawdown = (prices - rolling_max) / rolling_max

    max_dd = abs(drawdown.min())

    return f"最大回撤 {max_dd:.2%}"


@tool("calculate_volatility")
def calculate_volatility(symbol: str) -> str:
    """
    根据股票代码计算波动率
    """

    df = fetch_stock_data_robust(symbol)

    if df.empty:
        return "数据获取失败"

    prices = df["收盘"]

    returns = prices.pct_change().dropna()

    volatility = returns.std()

    return f"波动率 {volatility:.2%}"