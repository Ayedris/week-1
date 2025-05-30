import pytest
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import yfinance as yf
import pandas as pd

def test_sentiment_score():
    analyzer = SentimentIntensityAnalyzer()
    sentence = "The product launch was a massive success and stock prices soared."
    sentiment = analyzer.polarity_scores(sentence)
    assert isinstance(sentiment, dict)
    assert 'compound' in sentiment
    assert sentiment['compound'] > 0  # should be positive sentiment

def test_stock_data_download():
    df = yf.download("AAPL", period="3d")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "Close" in df.columns