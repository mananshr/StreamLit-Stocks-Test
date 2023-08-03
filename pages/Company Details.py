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
path = 'D:\\Code\\PY\\StreamlitTest2\\'
# print(info)

column1, column2, column3 = st.columns([2, 1, 1], gap="large")
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
    if sector is not None:
        "Sector:"
        f"### {sector}"
    if industry is not None:
        "Industry:"
        f"#### {industry}"
with column3:
    exchange = info.get("exchange")
    "Exchange:"
    f"### {exchange}"
    quoteType = info.get("quoteType")
    "Quote type:"
    f"#### {quoteType}"

column1, column2, column3 = st.columns(3)
current_price = info.get("currentPrice")
fiftyTwoWeekLow = info.get("fiftyTwoWeekLow")
fiftyTwoWeekHigh = info.get("fiftyTwoWeekHigh")
column1.metric("Current Price", f"$ {current_price}")
diff = current_price-fiftyTwoWeekHigh
diff = round(diff, 4)
column2.metric("Year High", f"$ {fiftyTwoWeekHigh}", diff, help="Compared to current price")
diff = current_price-fiftyTwoWeekLow
diff = round(diff, 4)
column3.metric("Year low", f"$ {fiftyTwoWeekLow}", diff, help="Compared to current price")

dayLow = info.get("dayLow")
dayHigh = info.get("dayHigh")
ask = info.get("ask")
column1.metric("Ask", f"$ {ask}")
diff = current_price-dayHigh
diff = round(diff, 4)
column2.metric("Day High", f"$ {dayHigh}", diff, help="Compared to current price")
diff = current_price-dayLow
diff = round(diff, 4)
column3.metric("Day low", f"$ {dayLow}", diff, help="Compared to current price")

longBusinessSummary = info.get("longBusinessSummary")
if longBusinessSummary is not None:
    st.write(longBusinessSummary)

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
        image = resize_image(image, image=image, length=1080)
        age = companyOfficer.get("age")
        yearBorn = companyOfficer.get("yearBorn")
        pay = companyOfficer.get("totalPay")
        fiscal = companyOfficer.get("fiscalYear")
        # image.
        column1.image(image)
        with column2:
            f"### {companyOfficerName}"
            f"#### {companyOfficerTitle}"
            if age is not None:
                f"**Age:** {age} ({yearBorn})"
            if pay is not None:
                pay = "{:,.2f}".format(pay)
                f"**Salary drawn:** $ {pay} ({fiscal})"
except Exception as exc:
    print(exc)
    "#### No officers listed here"



