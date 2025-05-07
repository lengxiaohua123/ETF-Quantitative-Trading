class BaseStrategy:
    def __init__(self, params=None):
        self.params = params or {}

    def generate_signals(self, data):
        raise NotImplementedError("请在子类中实现generate_signals方法")

    def set_params(self, params):
        self.params = params