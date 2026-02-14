import yfinance as yf

def load_data(symbol="BTC-USD", period="2y"):
    df = yf.download(symbol, period=period)
    return df
