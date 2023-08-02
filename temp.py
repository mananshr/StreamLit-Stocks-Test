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

# For testing
# counter = 0

# class MyDownloader(ImageDownloader):
#
#     def get_filename(self, task, default_ext):
#         url_path = urlparse(task['file_url'])[2]
#         if '.' in url_path:
#             extension = url_path.split('.')[-1]
#             if extension.lower() not in [
#                     'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
#             ]:
#                 extension = default_ext
#         else:
#             extension = default_ext
#         # works for python3
#         filename = base64.b64encode(url_path.encode()).decode()
#         # filename = url_path.split('/')[-1]
#
#         return '{}.{}'.format(filename, extension)

# symbols = ["V"]

for symbol in symbols:
    ticker_data = yfinance.Ticker(symbol)
    info = ticker_data.info
    companyName = info.get("longName")
    companyOfficers = info.get("companyOfficers")

    for companyOfficer in companyOfficers:
        companyOfficerName = companyOfficer.get("name")
        filters = dict(type='face')
        google_crawler = GoogleImageCrawler(feeder_threads=1, parser_threads=1, downloader_threads=1, storage={'root_dir': 'images\\'+symbol+"\\"+companyOfficerName})
        keyword = companyOfficerName + ", " + companyName
        print("Query: "+keyword)
        google_crawler.crawl(keyword, max_num=1, filters=filters)
        # path = 'D:\Code\PY\StreamlitTest2\\'
        # image_path = path+"images\\"+symbol
        # image_path = image_path + "\\" + os.listdir(image_path)[0]
        # # print("")
        # print("PATH: "+image_path)
