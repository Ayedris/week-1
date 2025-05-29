import yfinance as yf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime, timedelta

# Step 1: Sample headline
headline = "Apple stock hits record high as earnings beat expectations!"

# Step 2: Sentiment analysis
analyzer = SentimentIntensityAnalyzer()
sentiment_score = analyzer.polarity_scores(headline)
print("Sentiment Score:", sentiment_score)

# Step 3: Download stock data using yfinance
stock_symbol = "AAPL"
today = datetime.now()
start_date = today - timedelta(days=5)
end_date = today

data = yf.download(stock_symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
print("\nRecent Stock Prices for AAPL:\n", data[['Close']])
