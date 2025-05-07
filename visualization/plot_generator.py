import matplotlib.pyplot as plt

def plot_equity_curve(equity_curve, title="收益曲线"):
    plt.figure(figsize=(10,5))
    plt.plot(equity_curve)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Equity")
    plt.show()