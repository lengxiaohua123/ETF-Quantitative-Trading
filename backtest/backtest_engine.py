class BacktestEngine:
    def __init__(self, strategy, data, initial_cash=1000000, commission=0.001, slippage=0.0005):
        self.strategy = strategy
        self.data = data
        self.initial_cash = initial_cash
        self.commission = commission
        self.slippage = slippage

    def run(self):
        signals = self.strategy.generate_signals(self.data)
        # 伪代码：仅演示信号输出
        # 实际应有完整的资金、持仓、交易、绩效计算
        return signals