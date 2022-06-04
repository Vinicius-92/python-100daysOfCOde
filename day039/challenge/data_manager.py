import requests

SHEETY = "https://api.sheety.co/6a545d96b4a5f718b409011d51cc2c35/flightDeals/prices"
HEADER = {"Authorization": "Basic dmluaWNpdXM5MmFzOmxpc3RlbnRveW91cmhlYXJ0"}


class DataManager:

    def __init__(self):
        self.header = HEADER
        self.url = SHEETY

    def get_data(self):
        response = requests.get(self.url, headers=self.header)
        response.raise_for_status()
        return response.json()["prices"]
