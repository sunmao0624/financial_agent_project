import akshare as ak
import pandas as pd


def fetch_stock_data_robust(symbol: str) -> pd.DataFrame:
    """
    高可用行情获取模块，包含降级兜底机制。
    """
    # 链路 1：尝试东方财富主接口
    try:
        df = ak.stock_zh_a_hist(symbol=symbol, period="daily", adjust="qfq")
        if not df.empty:
            return df
    except Exception as e:
        print(f"[数据层告警] 东方财富接口阻断 ({e})，触发降级策略...")

    # 链路 2：无缝降级至新浪财经备用接口
    try:
        # 新浪接口要求代码附带市场标识前缀 (sz/sh)
        market_prefix = "sz" if symbol.startswith(('0', '3')) else "sh"
        full_symbol = f"{market_prefix}{symbol}"

        df = ak.stock_zh_a_daily(symbol=full_symbol, adjust="qfq")

        if not df.empty:
            # 抹平底层接口差异：将新浪返回的英文字段映射为系统的标准中文字段
            rename_map = {
                'date': '日期', 'open': '开盘', 'high': '最高',
                'low': '最低', 'close': '收盘', 'volume': '成交量'
            }
            df.rename(columns=rename_map, inplace=True)
            # 确保日期列的数据类型标准一致
            df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%Y-%m-%d')
            return df
    except Exception as e:
        print(f"[数据层告警] 备用新浪接口同样失败: {e}")

    # 彻底熔断，返回空数据帧防止程序向下抛出异常
    return pd.DataFrame()