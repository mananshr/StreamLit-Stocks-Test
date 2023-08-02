import yfinance
from icrawler.builtin import GoogleImageCrawler

symbols = [
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
        "TM"]

for symbol in symbols:
    ticker_data = yfinance.Ticker(symbol)
    info = ticker_data.info
    companyName = info.get("longName")
    google_crawler = GoogleImageCrawler(feeder_threads=1, parser_threads=1, downloader_threads=1,
                                        storage={'root_dir': 'images\\'+symbol+"\\logo"})
    filters = dict(size='large')
    keyword = companyName + " logo"
    print("Query: "+keyword)
    google_crawler.crawl(keyword, max_num=1)
