import numpy as np

def add_features(df):

    df['return_1'] = df['Close'].pct_change()
    df['return_3'] = df['Close'].pct_change(3)
    df['return_5'] = df['Close'].pct_change(5)

    df['ma_5'] = df['Close'].rolling(5).mean()
    df['ma_10'] = df['Close'].rolling(10).mean()
    df['ma_ratio'] = df['ma_5'] / df['ma_10']

    df['volatility_5'] = df['return_1'].rolling(5).std()
    df['volatility_10'] = df['return_1'].rolling(10).std()

    df.dropna(inplace=True)

    return df
