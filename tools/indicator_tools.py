import pandas as pd
from crewai.tools import tool
from .data_router import fetch_stock_data_robust
import json


@tool("calculate_indicators")
def calculate_indicators(symbol: str) -> str:
    """
    计算技术指标:
    MA5
    MA10
    RSI
    MACD
    """
    df = fetch_stock_data_robust(symbol)
    if df.empty:
        return "数据获取失败，无法计算技术指标"
    close = df["收盘"]
    # ======================
    # MA
    # ======================
    df["MA5"] = close.rolling(window=5).mean()
    df["MA10"] = close.rolling(window=10).mean()
    # ======================
    # RSI
    # ======================
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    # ======================
    # MACD
    # ======================
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    df["MACD"] = ema12 - ema26
    # ======================
    # 最新数据
    # ======================
    last = df.iloc[-1]
    ma5 = round(last["MA5"], 2)
    ma10 = round(last["MA10"], 2)
    rsi = round(last["RSI"], 2)
    macd = round(last["MACD"], 2)
    # ======================
    # 趋势判断
    # ======================
    ma_signal = "多头排列" if ma5 > ma10 else "空头排列"
    if rsi > 70:
        rsi_signal = "超买"
    elif rsi < 30:
        rsi_signal = "超卖"
    else:
        rsi_signal = "正常"
    # ======================
    # 返回结构化结果
    # ======================
    return json.dumps(
        {
            "ma5": ma5,
            "ma10": ma10,
            "rsi": rsi,
            "macd": macd,
            "ma_signal": ma_signal,
            "rsi_signal": rsi_signal
        },
        ensure_ascii=False
    )