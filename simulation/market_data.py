class MarketData:
    def __init__(self):
        self.data = {}

    def update(self, symbol, data):
        self.data[symbol] = data

    def get(self, symbol):
        return self.data.get(symbol, None)