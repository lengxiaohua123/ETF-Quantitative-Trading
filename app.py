import argparse
from apis import data_api, strategy_api, backtest_api, simulation_api, visualization

def main():
    parser = argparse.ArgumentParser(description="ETF Quantitative Trading Framework")
    parser.add_argument('--mode', choices=['api', 'cli'], default='cli', help='启动方式')
    args = parser.parse_args()
    if args.mode == 'api':
        # 启动API服务（例如使用FastAPI或Flask，未实现）
        print("API模式启动（待实现）")
    else:
        # CLI模式示例
        print("CLI工具启动")
        # 可扩展CLI命令

if __name__ == "__main__":
    main()
