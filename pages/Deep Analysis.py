import os

import streamlit as st
import yfinance
import pandas as pd
import numpy as np

symbol = "AAPL"

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

try:
    ticker_data = yfinance.Ticker(symbol)
    ticker_df = ticker_data.history(period="max")
    info = ticker_data.info
    stock_name = info.get("longName")
    f"## {stock_name}"
    column1, column2 = st.columns(2)
    with column1:
        f"####  Historic Closing Price Chart"
        st.line_chart(ticker_df["Close"])
    with column2:
        f"#### Historic Volume Chart"
        st.line_chart(ticker_df["Volume"])
except Exception as exc:
    print(exc)


