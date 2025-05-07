from .base_strategy import BaseStrategy
import pandas as pd

class MomentumStrategy(BaseStrategy):
    def generate_signals(self, data: pd.DataFrame):
        window = self.params.get("window", 10)
        data['momentum'] = data['close'].diff(window)
        data['signal'] = 0
        data.loc[data['momentum'] > 0, 'signal'] = 1
        data.loc[data['momentum'] < 0, 'signal'] = -1
        return data[['signal']]