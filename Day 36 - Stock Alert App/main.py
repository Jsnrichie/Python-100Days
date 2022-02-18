import requests
import itertools
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# ----------------------  KEYS and CONSTANTS  ---------------------- #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_API = 
# alpha_API = os.environ.get("alpha_API")
news_API = 

account_sid =
auth_token = 

# ----------------------  ACCESS STOCK DATA  ---------------------- #
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_API,
    "outputsize": "compact"
}

response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data = dict(itertools.islice(data.items(), 2))
stock_data = [value for (key, value) in data.items()]

# --------------------------------------  CALC PERCENT CHANGE  --------------------------------------------- #
current_day_open = float(stock_data[0]["1. open"])
previous_day_open = float(stock_data[1]["1. open"])
percent_change = (current_day_open - previous_day_open) / previous_day_open


# ----------------------  SEND ARTICLES IF THERE WAS A SIGNIFICANT CHANGE IN PRICE  ---------------------- #
if percent_change <= -0.01 or percent_change >= 0.01:
    if percent_change > 0:
        op_mes = f"{STOCK}: 🔺{round(percent_change * 100, 2)}%"
    else:
        percent_change *= -1
        op_mes = f"{STOCK}: 🔻{round(percent_change * 100, 2)}%"


    news_params = {
        "apiKey": news_API,
        "q": "tesla",
        "pageSize": 3
    }

    response = requests.get(url="https://newsapi.org/v2/top-headlines", params=news_params)
    response.raise_for_status()

    data = response.json()
    articles = data["articles"]

    client = Client(account_sid, auth_token)

    for page in articles:
        message = client.messages \
            .create(
            body=f"\n{op_mes}\nArticle from {page['source']['name']}\n\nHEADLINE: {page['title']}\n\n{page['url']}",
            from_='',
            to=''
        )

        print(message.status)
