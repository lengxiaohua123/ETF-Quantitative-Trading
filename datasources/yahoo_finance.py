import yfinance as yf
import pandas as pd

class YahooFinanceDataSource:
    def get_daily(self, symbol, start_date, end_date):
        df = yf.download(symbol, start=start_date, end=end_date)
        df.reset_index(inplace=True)
        return df