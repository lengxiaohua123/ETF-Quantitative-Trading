from backtest.backtest_engine import BacktestEngine

def run_backtest(strategy, data, config):
    engine = BacktestEngine(strategy, data, config['initial_cash'], config['commission_rate'], config['slippage'])
    results = engine.run()
    return results