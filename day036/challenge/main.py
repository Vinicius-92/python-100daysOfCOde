import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "E3QKIIT6Q6879PE3"
}

news_params = {
    "q": "Tesla",
    "apiKey": "c604dd3ab17842c8ab8ac7a046f5e2ee",
    "sortBy": "popularity",
    "pageSize": 3
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

days = response.json()["Time Series (Daily)"]
last_two_days_evaluation = []
for key in days:
    if len(last_two_days_evaluation) < 2:
        last_two_days_evaluation.append(abs(float(days[key]["4. close"])))

today = last_two_days_evaluation[0]
yesterday = last_two_days_evaluation[1]
difference = last_two_days_evaluation[0] - yesterday
percentage = difference / today * 100

if percentage > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    for art in articles:
        proxy_client = TwilioHttpClient()
        client = Client(
            "AC5cacfc92e513aac460346c0dffe23cf7",
            "6b02ce70b44962fe0099f024825fb63c",
            http_client=proxy_client)
        message = client.messages \
            .create(
                    body=f"(TSLA - %{percentage})\nHeadline: {art['title']}\nBrief: {art['description']}",
                    from_='+19594009207',
                    to='+5519996359084')
