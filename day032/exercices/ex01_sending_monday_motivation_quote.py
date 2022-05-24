import datetime as dt
import smtplib
import random

MY_EMAIL = "vsavgft@gmail.com"
PASSWORD = "Gftadmin#2021"

with open("quotes.txt", mode="r") as file:
    quotes = file.readlines()


def sendmail():
    quote_of_the_day = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="vinicius92as@yahoo.com",
            msg=f"Subject:Quote of the day\n\n{quote_of_the_day}."
        )


if dt.datetime.now().weekday() == 0:
    sendmail()
