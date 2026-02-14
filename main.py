import sys
from data_loader import load_data
from features import add_features
from model import train_models
from sentiment import get_fear_greed
#from news_sentiment import get_news_sentiment  
from report import create_report
from email_sender import send_email

EMAIL = "your_email"
PASSWORD = "your_password"
RECEIVER = "receiver email"

def main():
   
    if len(sys.argv) > 1:
        symbol = sys.argv[1]
    else:
       
        symbol = input("Enter trading symbol (e.g., BTC-USD): ")

    print(f"Running pipeline for symbol: {symbol}")

    # ===== pipeline =====
    df = load_data(symbol)
    df = add_features(df)
    lr_prob, rf_prob = train_models(df)

    fear_greed = get_fear_greed()
    #news_sentiment = 0.0 

    create_report(df, symbol, lr_prob, rf_prob, fear_greed)

    send_email("report.html", EMAIL, PASSWORD, RECEIVER)

    print("Pipeline finished ✅")

if __name__ == "__main__":
    main()
