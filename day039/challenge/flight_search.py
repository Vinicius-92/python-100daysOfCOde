import datetime
import requests

FLIGHT_SEARCH_URL = "https://tequila-api.kiwi.com/v2/search"
HEADER = {"apikey": "RzKqV2TH_PYjHjW7vgAV5ZgLO-xYcWrr"}


class FlightSearch:

    @staticmethod
    def get_flights(destination_code, min_price):
        today_date = datetime.date.today().strftime("%d/%m/%Y")
        today_plus_6_months = (datetime.date.today() + datetime.timedelta(days=365.25 / 2)).strftime("%d/%m/%Y")
        params = {
            "fly_from": "LCY",
            "fly_to": destination_code,
            "date_from": today_date,
            "date_to": today_plus_6_months
        }
        response_flight = requests.get(FLIGHT_SEARCH_URL, params=params, headers=HEADER)
        response_flight.raise_for_status()
        result = []
        for res in response_flight.json()["data"]:
            if res["price"] < min_price:
                result.append(res)
        return result
