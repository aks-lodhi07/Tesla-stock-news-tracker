from http.client import responses

import requests
from twilio.rest import Client


from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env file

STOCK = os.getenv("STOCK")
COMPANY_NAME = os.getenv("COMPANY_NAME")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACC_SID = os.getenv("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")
TWILIO_TO = os.getenv("TWILIO_TO")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":ALPHA_VANTAGE_API_KEY
}
stock_response=requests.get(url=STOCK_ENDPOINT,params=stock_params)
stock_response.raise_for_status()
data=stock_response.json()["Time Series (Daily)"]
data_list=[value for key,value in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
data_of_day_before_yesterday=data_list[1]
day_before_yesterday_closing_price=data_of_day_before_yesterday["4. close"]

price_difference=abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
percentage_difference=(price_difference/float(yesterday_closing_price))*100

if percentage_difference>0:
    news_parameters={
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME
    }
    news_response=requests.get(url=NEWS_ENDPOINT,params=news_parameters)
    news_response.raise_for_status()
    articles=news_response.json()["articles"]
    three_articles=articles[:3]
    print(f"Total articles fetched: {len(articles)}")
    print(f"Articles used: {len(three_articles)}")

    formatted_articles = [
        f"TSLA:{article['title']}\nBrief: {article['description']}"
        for article in three_articles
    ]
    for article in formatted_articles:
        client=Client(TWILIO_ACC_SID,TWILIO_AUTH_TOKEN)
        message=client.messages.create(
            body=article,
            from_=TWILIO_FROM,
            to=TWILIO_TO
        )
    print(f"Message sent with SID: {message.sid}")
    print(f"Status: {message.status}")