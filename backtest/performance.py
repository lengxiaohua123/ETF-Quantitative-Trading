def calc_performance(equity_curve):
    # 简单绩效指标计算示例
    annual_return = (equity_curve[-1] / equity_curve[0]) ** (252 / len(equity_curve)) - 1
    max_drawdown = ((equity_curve.cummax() - equity_curve) / equity_curve.cummax()).max()
    return {"annual_return": annual_return, "max_drawdown": max_drawdown}