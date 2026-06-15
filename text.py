import akshare as ak


print("正在尝试获取晶澳科技(002459)数据...")
try:
    df = ak.stock_zh_a_hist_163(symbol=symbol)
    if not df.empty:
        print("✅ 数据获取成功！")
        print(df.tail(5))
    else:
        print("❌ 获取到了空数据")
except Exception as e:
    print(f"❌ 发生错误: {e}")