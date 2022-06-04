from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


class NotificationManager:

    @staticmethod
    def send_message(price, destination):
        proxy_client = TwilioHttpClient()
        client = Client(
            "AC5cacfc92e513aac460346c0dffe23cf7",
            "6b02ce70b44962fe0099f024825fb63c",
            http_client=proxy_client)
        message = client.messages \
            .create(
            body=f"Ahoy, let's travel! Destination: {destination}, Price: U${price}",
            from_='+19594009207',
            to='+5519996359084')
