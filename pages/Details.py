import os

import streamlit as st
import yfinance
from PIL import Image
from icrawler.builtin import GoogleImageCrawler

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
#
# google_crawler = GoogleImageCrawler(feeder_threads=1, parser_threads=1, downloader_threads=1, storage={'root_dir': 'images\\'+symbol})
# google_crawler.crawl(keyword=companyOfficerName, max_num=1)

#pages")
path = 'D:\Code\PY\StreamlitTest2\\'
# image_path = os.getcwd()+"\\images\\"+symbol+"\\000001.jpg"
image_path = path+"images\\"+symbol+"\\"+companyOfficerName
image_path = image_path + "\\" + os.listdir(image_path)[0]
# print("")
print("PATH: "+image_path)
# image_path = image_path.replace("\\\\","\\")
image = Image.open(image_path)
column1, column2 = st.columns(2)
with column1:
    st.image(image)
with column2:
    f"## {companyOfficerName}"


# class MyImageDownloader(ImageDownloader):
#     def get_filename(self, task, default_ext):
#         url_path = urlparse(task['file_url'])[2]
#         # print("Person: "+companyOfficerName)
#         print("URL: "+url_path)
#         if '.' in url_path:
#             extension = url_path.split('.')[-1]
#             if extension.lower() not in [
#                 'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
#             ]:
#                 extension = default_ext
#         else:
#             extension = default_ext
#         # works for python3
#         filename = base64.b64encode(url_path.encode()).decode()
#         print("File: "+filename)
#         return '{}.{}'.format(filename, extension)

# google_crawler = GoogleImageCrawler(feeder_threads=1, parser_threads=1, downloader_threads=1, storage={'root_dir': 'images\\'+symbol}, downloader_cls=MyImageDownloader)

# directory = os.getcwd()
# print(directory)


