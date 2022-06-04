import smtplib

from twilio.rest import Client

TWILIO_SID = "AC5cacfc92e513aac460346c0dffe23cf7"
TWILIO_AUTH_TOKEN = "6b02ce70b44962fe0099f024825fb63c"
TWILIO_VIRTUAL_NUMBER = "+19594009207"
TWILIO_VERIFIED_NUMBER = "+5519996359084"
MY_EMAIL = "vsavgft@gmail.com"
MY_PASSWORD = "Gftadmin#2021"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    @staticmethod
    def send_emails(emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
