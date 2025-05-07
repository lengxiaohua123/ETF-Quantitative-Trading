from .base_strategy import BaseStrategy
import pandas as pd

class MovingAverageStrategy(BaseStrategy):
    def generate_signals(self, data: pd.DataFrame):
        data['ma_short'] = data['close'].rolling(window=self.params.get("short_window", 5)).mean()
        data['ma_long'] = data['close'].rolling(window=self.params.get("long_window", 20)).mean()
        data['signal'] = 0
        data.loc[data['ma_short'] > data['ma_long'], 'signal'] = 1
        data.loc[data['ma_short'] < data['ma_long'], 'signal'] = -1
        return data[['signal']]