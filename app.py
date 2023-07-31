import datetime

import streamlit as st
import yfinance

"# Stock Markets Today"

symbol = "AAPL"

column1, column2, column3 = st.columns(3)

with column1:
    symbol = st.selectbox(
        "Select a stock to analyse",
        (
            "TM",
            "MCD",
            "ACN",
            "ADBE",
            "BABA",
            "KO",
            "ORCL",
            "JNJ",
            "MA",
            "PG",
            "WMT",
            "V",
            "TSM",
            "BRK-A",
            "JPM",
            "GILD",
            "ADP",
            "CSCO",
            "INTC",
            "AMGN",
            "AMD",
            "AVGO",
            "AMZN",
            "CMCSA",
            "NVDA",
            "META",
            "AAPL",
            "MSFT",
            "GOOG",
            "TSLA",
            "SPPI",
            "NFLX",
        ),
    )

with column2:
    start_date = st.date_input("Start Date: ", datetime.date(2016, 1, 1))

with column3:
    end_date = st.date_input("End Date: ", datetime.date(2019, 1, 1))

ticker_data = yfinance.Ticker(symbol)

info = ticker_data.info
# info
stock_name = info.get("longName")
st.divider()
f"**{stock_name}** data from {start_date} to {end_date}"
ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)
st.dataframe(ticker_df, use_container_width=True)
st.divider()
f"#### {stock_name}'s Closing Price Chart"
st.line_chart(ticker_df["Close"])
f"#### {stock_name}'s Volume Chart"
st.line_chart(ticker_df["Volume"])
