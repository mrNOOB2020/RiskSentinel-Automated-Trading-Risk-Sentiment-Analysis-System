import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def create_report(df, symbol, lr_prob, rf_prob, fear_greed):
    """
    ساخت گزارش کامل: Risk Metrics + ML Prediction + Sentiment + Equity Curve
    """

    # ===== Equity Curve =====
    equity = (1 + df['return_1']).cumprod()

    plt.figure(figsize=(8,4))
    plt.plot(equity, label='Equity Curve')
    plt.title(f"{symbol} Equity Curve")
    plt.xlabel("Days")
    plt.ylabel("Equity")
    plt.legend()
    plt.tight_layout()
    plt.savefig("equity.png")
    plt.close()

    # ===== Risk Metrics =====
    returns = df['return_1']
    volatility = returns.std() * np.sqrt(252)
    sharpe = (returns.mean() / returns.std()) * np.sqrt(252)
    max_dd = ((equity.cummax() - equity) / equity.cummax()).max()
    final_equity = equity.iloc[-1]
    var_95 = np.percentile(returns, 5)

    # ===== HTML Report =====
    html = f"""
<h1>Daily Trading Report</h1>
<p><b>Symbol:</b> {symbol}</p>
<p><b>Date:</b> {datetime.today()}</p>

<h2>Risk Metrics</h2>
<ul>
<li>Volatility: {volatility:.4f}</li>
<li>VaR 95%: {var_95:.4f}</li>
<li>Max Drawdown: {max_dd:.4f}</li>
<li>Sharpe Ratio: {sharpe:.2f}</li>
<li>Final Equity: ${final_equity:.2f}</li>
</ul>

<h2>ML Prediction</h2>
<ul>
<li>Probability of loss tomorrow (Logistic): {lr_prob:.2f}</li>
<li>Probability of loss tomorrow (RandomForest): {rf_prob:.2f}</li>
</ul>

<h2>Sentiment Analysis</h2>
<ul>
<li>Fear & Greed Index: {fear_greed}</li>

</ul>

<h2>Equity Curve</h2>
<img src="cid:equity" width="700">

"""

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)
