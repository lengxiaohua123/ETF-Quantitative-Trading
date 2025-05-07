class AccountManager:
    def __init__(self, initial_cash):
        self.cash = initial_cash
        self.positions = {}

    def update_cash(self, amount):
        self.cash += amount

    def update_position(self, symbol, volume):
        self.positions[symbol] = self.positions.get(symbol, 0) + volume

    def get_account_info(self):
        return {"cash": self.cash, "positions": self.positions}