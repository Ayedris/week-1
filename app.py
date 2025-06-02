import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
data_dir = "notebooks/processed"
stock_files = [f for f in os.listdir(data_dir) if f.endswith("_indicators.xlsx")]
stock_names = [f.split("_historical_data")[0] for f in stock_files]

# Sidebar selection
st.sidebar.title("Stock Dashboard")
selected_stock = st.sidebar.selectbox("Select a stock:", stock_names)

# Load selected stock data
file_path = os.path.join(data_dir, f"{selected_stock}_historical_data_indicators.xlsx")
df = pd.read_excel(file_path, index_col="Date", parse_dates=True)

# Title
st.title(f"{selected_stock} Technical Indicators Dashboard")

# Plot 1: Close + SMA
st.subheader("Close Price and SMA")
fig, ax = plt.subplots()
ax.plot(df.index, df['Close'], label='Close Price')
ax.plot(df.index, df['SMA_20'], label='SMA 20', color='orange')
ax.legend()
st.pyplot(fig)

# Plot 2: RSI
st.subheader("RSI")
fig, ax = plt.subplots()
ax.plot(df.index, df['RSI'], color='purple')
ax.axhline(70, color='red', linestyle='--')
ax.axhline(30, color='green', linestyle='--')
ax.set_ylabel("RSI")
st.pyplot(fig)

# Plot 3: MACD
st.subheader("MACD")
fig, ax = plt.subplots()
ax.plot(df.index, df['MACD'], label='MACD', color='blue')
ax.plot(df.index, df['MACD_signal'], label='Signal', color='orange')
ax.legend()
st.pyplot(fig)
