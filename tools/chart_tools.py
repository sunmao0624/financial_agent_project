import json
import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from crewai.tools import tool
import os
from tools.data_router import fetch_stock_data_robust


@tool("generate_professional_chart")
def generate_professional_chart(symbol: str) -> str:
    """获取数据生成图表"""
    try:
        df = fetch_stock_data_robust(symbol)
        if df.empty:
            return f"生成图表失败：无法获取股票 {symbol} 数据。"

        recent_df = df.tail(60).copy()
        recent_df['日期'] = pd.to_datetime(recent_df['日期'])
        recent_df.set_index('日期', inplace=True)

        # 计算均线
        recent_df['MA5'] = recent_df['收盘'].rolling(5).mean()
        recent_df['MA10'] = recent_df['收盘'].rolling(10).mean()

        # 2. 图表样式配置：采用学术级高分辨率与专业排版
        plt.style.use('seaborn-v0_8-paper')
        plt.rcParams['figure.dpi'] = 300  # 高分辨率
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
        plt.rcParams['axes.unicode_minus'] = False

        # 专业调色板
        colors = sns.color_palette("deep")

        # 3. 创建多子图布局 (上图走势，下图成交量)
        fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(10, 8), sharex=True)
        fig.subplots_adjust(hspace=0.05)  # 缩小上下图间距

        # --- 子图 1: 价格与均线 ---
        ax1.plot(recent_df.index, recent_df['收盘'], label='收盘价', color=colors[0], linewidth=1.5)
        ax1.plot(recent_df.index, recent_df['MA5'], label='MA5', color=colors[1], linestyle='--', alpha=0.8)
        ax1.plot(recent_df.index, recent_df['MA10'], label='MA10', color=colors[2], linestyle='-.', alpha=0.8)

        ax1.set_title(f'股票 {symbol} 行情量价分析', fontsize=14, fontweight='bold', pad=15)
        ax1.set_ylabel('价格 (元)', fontsize=11)
        ax1.legend(loc='upper left', frameon=True, edgecolor='black')
        ax1.grid(True, linestyle=':', alpha=0.6)

        # --- 子图 2: 成交量 ---
        ax2.bar(recent_df.index, recent_df['成交量'], color=colors[3], alpha=0.7, width=0.6)
        ax2.set_ylabel('成交量', fontsize=11)
        ax2.grid(True, linestyle=':', alpha=0.6)

        # 设置X轴日期格式
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45)

        # 4. 保存图表
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        img_path = os.path.join(output_dir, f"{symbol}_chart.png")

        plt.savefig(img_path, bbox_inches='tight')
        plt.close()

        # 5. 返回供 Markdown 使用的链接
        return f"图表生成成功。请在研报中直接插入这行代码：\n\n![{symbol} 行情图表]({img_path})\n"

    except Exception as e:
        return f"生成图表失败: {str(e)}"