import streamlit as st
import yfinance
from icrawler.builtin import GoogleImageCrawler
from icrawler import ImageDownloader

import os

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

# def deleteImages():
#    os.remove(os.getcwd()+"\\images\\")

ticker_data = yfinance.Ticker(symbol)

info = ticker_data.info
longName = info.get("longName")
f"# {longName}"

companyOfficers = info.get("companyOfficers")
companyOfficerName = companyOfficers[0].get("name")

class MyImageDownloader(ImageDownloader):
    def get_filename(self, task, default_ext):
        filename = super(MyImageDownloader, self).get_filename(
            task, default_ext)
        print(filename)
        return '{}_{}'.format(filename, default_ext)

google_crawler = GoogleImageCrawler(feeder_threads=1, parser_threads=1, downloader_threads=1, storage={'root_dir': 'images\\'+symbol}, downloader_cls=MyImageDownloader)
google_crawler.crawl(keyword=companyOfficerName, max_num=1)

# directory = os.getcwd()
# print(directory)


