import streamlit as st
import yfinance

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
        "SPPI",
        "TSLA",
        "TSM",
        "V",
        "WMT",
        "TM",
    ),
)

ticker_data = yfinance.Ticker(symbol)

info = ticker_data.info
longName = info.get("longName")
f"# {longName}"

companyOfficers = info.get("companyOfficers")
companyOfficerName = companyOfficers[0].get("name")
companyOfficerName
