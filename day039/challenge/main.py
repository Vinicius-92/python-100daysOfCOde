from day039.challenge.data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

dm = DataManager()
sheety_data = dm.get_data()
filtered_sheety_data = [{"iata": destiny.get("iataCode"), "price": destiny.get("lowestPrice")}
                        for destiny in sheety_data]

for destiny in filtered_sheety_data:
    flights_data = FlightSearch.get_flights(destination_code=destiny["iata"], min_price=destiny["price"])
    if len(flights_data) != 0:
        for flight in flights_data:
            NotificationManager.send_message(price=flight.get("price"), destination=flight.get("cityTo"))
