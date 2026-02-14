# RiskSentinel – Automated Trading Risk & Sentiment Analysis System

##  Project Overview
RiskSentinel is an automated financial data analysis and risk monitoring pipeline that combines:

- Market data collection
- Feature engineering
- Machine learning risk prediction
- Sentiment analysis (Fear & Greed + News)
- Performance metrics calculation
- Automated HTML report generation
- Email delivery
- Scheduled daily execution

The system helps traders and analysts evaluate portfolio risk and market sentiment before trading decisions.

---

##  Features

 Download historical price data using Yahoo Finance  
 Compute technical indicators & returns  
 Train ML models (Logistic Regression, Random Forest)  
 Estimate probability of loss for next day  
 Fetch Fear & Greed Index  
 News sentiment scoring  
 Risk metrics (Sharpe, Volatility, Max Drawdown, VaR)  
 Generate equity curve chart  
 Auto-generate HTML report  
 Send report via email  
 Can run automatically with Windows Task Scheduler  

---

##  Sample Report Output

The system generates an HTML report containing:

- Symbol
- Date
- Loss probability (LR & RF)
- Fear & Greed index
- News sentiment score
- Volatility
- Sharpe ratio
- Max drawdown
- Total return
- Equity curve chart

---

##  Project Structure
trading_automation/
│
├── main.py
├── data_loader.py
├── features.py
├── model.py
├── sentiment.py
├── report.py
├── email_sender.py
└── README.md
## How to Run
Install dependencies:
Run manually:
Or run without argument:

Then enter symbol manually.

---

##  Requirements

- Python 3.10+
- yfinance
- pandas
- numpy
- scikit-learn
- matplotlib
- requests

---

##  Use Cases

- Daily crypto risk monitoring
- Stock portfolio analysis
- Quant research projects
- Internship / academic demonstrations
- Automated trading risk dashboards

---

##  Author

Developed by [Hesam Hesari]

Financial Data Science | Machine Learning | Algorithmic Trading

