import argparse
from apis import data_api, strategy_api, backtest_api, simulation_api, visualization

def main():
    parser = argparse.ArgumentParser(description="ETF Quantitative Trading Framework")
    parser.add_argument('--mode', choices=['api', 'cli'], default='cli', help='启动方式')
    args = parser.parse_args()
    if args.mode == 'api':
        print("API模式启动（可扩展FastAPI/Flask等）")
    else:
        print("CLI模式启动")
        # 示例：命令行数据获取
        df = data_api.fetch_daily('000001.SZ', '20240101', '20240501')
        print(df.head())

if __name__ == "__main__":
    main()