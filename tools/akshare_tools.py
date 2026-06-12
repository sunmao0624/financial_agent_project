import json
import akshare as ak
from langchain.tools import tool


@tool("get_stock_data")
def get_stock_data(symbol: str) -> str:
    """
    获取A股最近30天行情数据
    """

    try:
        df = ak.stock_zh_a_hist(
            symbol=symbol,
            period="daily",
            adjust="qfq"
        )

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

    except Exception as e:
        return f"error:{str(e)}"