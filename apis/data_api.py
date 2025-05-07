from datasources.tushare import TushareDataSource
from utils.config_loader import load_config

config = load_config()
ds = TushareDataSource(token=config['data_sources']['tushare']['token'])

def fetch_daily(ts_code, start, end):
    df = ds.get_daily(ts_code, start, end)
    return df