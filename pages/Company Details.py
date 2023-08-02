import os

import streamlit as st
import yfinance
from PIL import Image

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

# def deleteImages():
#    os.remove(os.getcwd()+"\\images\\")

def resize_image(self, image: Image, length: int) -> Image:
    """
    Resize an image to a square. Can make an image bigger to make it fit or smaller if it doesn't fit. It also crops
    part of the image.

    Resizing strategy :
     1) We resize the smallest side to the desired dimension (e.g. 1080)
     2) We crop the other side so as to make it fit with the same length as the smallest side (e.g. 1080)


    :param self:
    :param image: Image to resize.
    :param length: Width and height of the output image.
    :return: Return the resized image.
    """
    if image.size[0] < image.size[1]:
        # The image is in portrait mode. Height is bigger than width.
        # This makes the width fit the LENGTH in pixels while conserving the ration.
        resized_image = image.resize((length, int(image.size[1] * (length / image.size[0]))))
        # Amount of pixel to lose in total on the height of the image.
        required_loss = (resized_image.size[1] - length)
        # Crop the height of the image so as to keep the center part.
        resized_image = resized_image.crop(
            box=(0, required_loss / 2, length, resized_image.size[1] - required_loss / 2))
        # We now have a length*length pixels image.
        return resized_image
    else:
        # This image is in landscape mode or already squared. The width is bigger than the heihgt.
        # This makes the height fit the LENGTH in pixels while conserving the ration.
        resized_image = image.resize((int(image.size[0] * (length / image.size[1])), length))
        # Amount of pixel to lose in total on the width of the image.
        required_loss = resized_image.size[0] - length
        # Crop the width of the image so as to keep 1080 pixels of the center part.
        resized_image = resized_image.crop(
            box=(required_loss / 2, 0, resized_image.size[0] - required_loss / 2, length))
        # We now have a length*length pixels image.
        return resized_image

ticker_data = yfinance.Ticker(symbol)

info = ticker_data.info
longName = info.get("longName")
f"# {longName}"
path = 'D:\Code\PY\StreamlitTest2\\'
# print(info)

column1, column2 = st.columns(2, gap="large")
with column1:
    image_path = path+"images\\"+symbol+"\\logo"
    image_path = image_path + "\\" + os.listdir(image_path)[0]
    image = Image.open(image_path)
    # new_image = Image.new("RGB", image.size, "WHITE") # Create a white rgba background
    # new_image.paste(image, mask=image)
    st.image(image)
with column2:
    industry = info.get("industry")
    sector = info.get("sector")
    if(sector!=None):
        f"## {sector}"
    if(industry!=None):
         f"### {industry}"

try:
    longBusinessSummary = info.get("longBusinessSummary")
    if(longBusinessSummary!=None):
        st.write(longBusinessSummary)
except:
    pass

# google_crawler = GoogleImageCrawler(feeder_threads=1,
# parser_threads=1, downloader_threads=1,
# storage={'root_dir': 'images\\'+symbol})
# google_crawler.crawl(keyword=companyOfficerName, max_num=1)

try:
    companyOfficers = info.get("companyOfficers")
    companyOfficerName = companyOfficers[0].get("name")
    companyOfficerTitle = companyOfficers[0].get("title")

    "# The Board"

    for i in range(len(companyOfficers)):
        companyOfficer = companyOfficers[i]
        # column1, column2 = st.columns(2)
        companyOfficerName = companyOfficer.get("name")
        companyOfficerTitle = companyOfficer.get("title")
        column1, column2 = st.columns(2)
        image_path = path+"images\\"+symbol+"\\"+companyOfficerName
        image_path = image_path + "\\" + os.listdir(image_path)[0]
        image = Image.open(image_path)
        image = resize_image(image,image=image, length=1080)
        # image.
        column1.image(image)
        with column2:
            f"### {companyOfficerName}"
            f"#### {companyOfficerTitle}"
except:
    "#### No officers listed here"
# # image_path = os.getcwd()+"\\images\\"+symbol+"\\000001.jpg"
# image_path = path+"images\\"+symbol+"\\"+companyOfficerName
# image_path = image_path + "\\" + os.listdir(image_path)[0]
# # print("")
# print("PATH: "+image_path)
# # image_path = image_path.replace("\\\\","\\")
# image = Image.open(image_path)
# column1, column2 = st.columns(2)
# with column1:
#     st.image(image)
# with column2:
#     f"## {companyOfficerName}"
#     f"### {companyOfficerTitle}"
#     with column2:
#         companyOfficerName = companyOfficer.get("name")
#         companyOfficerTitle = companyOfficer.get("title")
#         column3, column4 = st.columns(2)
#         with column3:
#             image_path = path+"images\\"+symbol+"\\"+companyOfficerName
#             image_path = image_path + "\\" + os.listdir(image_path)[0]
#             image = Image.open(image_path)
#             st.image(image)
#         with column4:
#             f"### {companyOfficerName}"
#             f"#### {companyOfficerTitle}"


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


