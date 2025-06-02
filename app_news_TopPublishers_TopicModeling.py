import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

# Load data
st.title("Financial News Insights Dashboard")

news_df = pd.read_csv("data/raw/financial_news.csv")
news_df['date'] = pd.to_datetime(news_df['date'])

# Top Publishers
st.subheader("Top 10 News Publishers")
top_publishers = news_df['publisher'].value_counts().head(10)
fig, ax = plt.subplots()
top_publishers.plot(kind='barh', ax=ax)
st.pyplot(fig)

# News Volume Over Time
st.subheader("Publication Volume Over Time (Daily)")
daily_counts = news_df.set_index('date').resample('D').size()
fig, ax = plt.subplots()
daily_counts.plot(ax=ax)
st.pyplot(fig)

# Keyword Analysis
st.subheader("Top Keywords in Headlines")
vectorizer = CountVectorizer(stop_words='english', max_features=20)
X = vectorizer.fit_transform(news_df['headline'].fillna(""))
top_keywords = pd.Series(X.toarray().sum(axis=0), index=vectorizer.get_feature_names_out())
fig, ax = plt.subplots()
top_keywords.sort_values().plot(kind='barh', ax=ax)
st.pyplot(fig)
