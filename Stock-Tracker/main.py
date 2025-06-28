import requests
import json
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "0VTVHI24E6CXGDBB"
NEWS_API_KEY = "8c153320e4d44b84b496bf3b1ac14b42"
TWILIO_API_KEY = "a6fdec7e73886d384b565831ecb92921"
TWILIO_NUMBER = "+18669134111"
TWILIO_USER_ID = "AC9b156d1b00a89801783537543af8b906"


def get_stock_info():
    current_date = datetime.now().date()
    yesterdays_date = current_date - timedelta(days=1)

    # <editor-fold desc="Use this code snippet if loading directly from stocks API">
    # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}'
    # r = requests.get(url)
    # data = r.json()

    # with open("stock_data.json", "w") as stock_file:
    #     json.dump(data, stock_file, indent=4)

    # <editor-fold desc="Use this code snippet if loading from a predefined JSON">
    data = {}
    with open("stock_data.json", "r") as stock_file:
        data = json.load(stock_file)
    # </editor-fold>

    todays_stock_data = data["Time Series (Daily)"][str(current_date)]
    yesterdays_stock_data = data["Time Series (Daily)"][str(yesterdays_date)]

    todays_open_price = float(todays_stock_data["1. open"])
    yesterdays_close_price = float(yesterdays_stock_data["4. close"])

    percent_diff = abs(todays_open_price - yesterdays_close_price) / ((todays_open_price + yesterdays_close_price) / 2) * 100

    if percent_diff <= -5 or percent_diff >= 5:
        return percent_diff
    else:
        return False


def get_stock_news(percent_diff):
    url = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&language=en&apiKey={NEWS_API_KEY}'
    r = requests.get(url)
    data = r.json()

    with open("news_data.json", "w") as news_file:
        json.dump(data, news_file, indent=4)

    articles = [data["articles"][i] for i in range(3)]

    send_sms(articles, percent_diff)


def send_sms(articles, percent_diff):
    message_body = ""
    headline_1 = articles[0]["title"]
    description_1 = articles[0]["description"]
    headline_2 = articles[1]["title"]
    description_2 = articles[1]["description"]

    if percent_diff > 5:
        message_body = f"""TSLA: 🔺{percent_diff}%
        Headline: {headline_1} 
        Brief: {description_1}
        Headline: {headline_2}
        Brief: {description_2}"""
    else:
        message_body = f"""TSLA: 🔻{percent_diff}%
        Headline: {headline_1} 
        Brief: {description_1}
        Headline: {headline_2}
        Brief: {description_2}"""

    print(message_body)
    client = Client(TWILIO_USER_ID, TWILIO_API_KEY)
    message = client.messages.create(
        body= message_body,
        from_= TWILIO_NUMBER,
        to="+13372947224",
    )

    print(f"SID: {message.sid} Status: {message.status}")

# Only send a message if the stock is at a marginal difference between days
if type(get_stock_info()) is not bool:
    get_stock_news(get_stock_info())


