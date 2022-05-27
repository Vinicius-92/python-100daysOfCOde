import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "AC5cacfc92e513aac460346c0dffe23cf7"
auth_token = "14715ba4b178c8406bbe2ba235a01944"
LAT = -22.5647
LON = -47.4017
params = {
    "lon": LON,
    "lat": LAT,
    "exclude": "current,daily,minutely",
    "appid": "0127edf0905bc42f2e4036089e6f85d8"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()

will_rain = False
list_of_forecasts = response.json()["hourly"][:12]
for hour in list_of_forecasts:
    if hour["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+19594009207',
        to='+5519996359084'
    )
    print(message.status)
