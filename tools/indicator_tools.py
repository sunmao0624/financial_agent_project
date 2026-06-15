import akshare as ak
import pandas as pd
from crewai.tools import tool


@tool("calculate_indicators")
def calculate_indicators(symbol: str) -> str:
    """
    计算 MA5 MA10 RSI
    """

    df = ak.stock_zh_a_hist(
        symbol=symbol,
        period="daily",
        adjust="qfq"
    )

    close = df["收盘"]

    df["MA5"] = close.rolling(5).mean()
    df["MA10"] = close.rolling(10).mean()

    delta = close.diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100 / (1 + rs))

    last = df.iloc[-1]

    return f"""
MA5:{last['MA5']}

MA10:{last['MA10']}

RSI:{last['RSI']}
"""