import json
from crewai.tools import tool
from .data_router import fetch_stock_data_robust  # 导入路由函数


@tool("get_stock_data")
def get_stock_data(symbol: str) -> str:
    """获取A股最近30天行情数据"""
    df = fetch_stock_data_robust(symbol)

    if df.empty:
        return f"获取股票 {symbol} 数据失败，请在报告中提示数据缺失。"

    recent = df.tail(30)
    result = []
    for _, row in recent.iterrows():
        result.append({
            "date": str(row["日期"]),
            "open": float(row["开盘"]),
            "close": float(row["收盘"]),
            "high": float(row["最高"]),
            "low": float(row["最低"]),
            "volume": float(row["成交量"])
        })
    return json.dumps(result, ensure_ascii=False)