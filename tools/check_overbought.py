from crewai.tools import tool

@tool("check_overbought")
def check_overbought(rsi: float):

    if rsi > 70:
        return "RSI超买"

    return "正常"