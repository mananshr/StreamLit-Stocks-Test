import datetime

import streamlit as st
import yfinance

"# Stock Markets"

symbol = "AAPL"

column1, column2, column3 = st.columns(3)

with column1:
    symbol = st.selectbox(
        "Select a stock to analyse",
        (
            "AAPL",
            "ACN",
            "ADBE",
            "ADP",
            "AMD",
            "AMZN",
            "AVGO",
            "BABA",
            "BRK-A",
            "CMCSA",
            "CSCO",
            "GILD",
            "GOOG",
            "INTC",
            "JNJ",
            "JPM",
            "KO",
            "MA",
            "MCD",
            "META",
            "MSFT",
            "NFLX",
            "NVDA",
            "ORCL",
            "PG",
            "TSLA",
            "TSM",
            "V",
            "WMT",
            "TM",
        ),
    )

with column2:
    start_date = st.date_input("Start Date: ", datetime.date(2016, 1, 1))

with column3:
    end_date = st.date_input("End Date: ", datetime.date.today())

ticker_data = yfinance.Ticker(symbol)

info = ticker_data.info

# info
stock_name = info.get("longName")
f"# {stock_name}"
column1, column2, column3 = st.columns([1, 1, 2])
with column1:
    current_price = info.get("currentPrice")
    open_price = info.get("open")
    diff_since_open = current_price - open_price
    diff_since_open = diff_since_open / 10
    diff_since_open = round(diff_since_open, 2)
    column1.metric("Current Price", f"$ {current_price}", diff_since_open)
with column2:
    # last_close = info.get("previousClose")
    diff_since_close = current_price - open_price
    diff_since_close = round(diff_since_close, 4)
    column2.metric("Opening", f"$ {open_price}", diff_since_close)
with column3:
    industry = info.get("industry")
    long_business_summary = info.get("longBusinessSummary")
    column3.metric("Industry", industry, help=long_business_summary)

st.divider()
# f"**{stock_name}** data from {start_date} to {end_date}"
ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)
# st.dataframe(ticker_df, use_container_width=True)
# st.divider()
f"#### {stock_name}'s Closing Price Chart"
st.line_chart(ticker_df["Close"])
f"#### {stock_name}'s Volume Chart"
st.line_chart(ticker_df["Volume"])
