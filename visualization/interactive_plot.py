import plotly.graph_objs as go

def plot_interactive_equity_curve(equity_curve):
    fig = go.Figure(data=[go.Scatter(y=equity_curve, mode='lines', name='Equity')])
    fig.update_layout(title='收益曲线', xaxis_title='Date', yaxis_title='Equity')
    fig.show()