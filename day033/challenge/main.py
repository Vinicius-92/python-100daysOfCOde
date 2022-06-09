import requests
import smtplib
import time
from datetime import datetime

MY_LONG = -47.404709
MY_LAT = -22.563021
MY_EMAIL = "ERASED FOR SECURITY"
MY_PASSWORD = "ERASED FOR SECURITY"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()


def is_near():
    if MY_LAT - 5 >= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 >= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():
    if sunset > time_now.hour < sunrise:
        return True


def check_if_its_near_and_its_dark():
    if is_dark() and is_near():
        return True


while True:
    if check_if_its_near_and_its_dark():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up!\n\nISS is above us."
            )
    time.sleep(60)
