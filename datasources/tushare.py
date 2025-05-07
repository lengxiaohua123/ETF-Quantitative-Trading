import tushare as ts

class TushareDataSource:
    def __init__(self, token):
        self.pro = ts.pro_api(token)

    def get_daily(self, ts_code, start_date, end_date):
        return self.pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)