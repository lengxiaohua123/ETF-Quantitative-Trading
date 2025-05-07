def select_stocks(strategy, data):
    signals = strategy.generate_signals(data)
    selected = data[signals['signal'] == 1]
    return selected