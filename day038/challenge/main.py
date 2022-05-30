import requests
from datetime import datetime

API_ID = "866d6616"
API_KEY = "aa1add723614c039d7b74cb10c68f1d9"
NUTRIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = "https://api.sheety.co/6a545d96b4a5f718b409011d51cc2c35/workoutTracking/workouts"

headers_nutrix = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
header_sheety = {
    "Authorization": "Basic dmluaWNpdXM5MmFzOmxpc3RlbnRveW91cmhlYXJ0"
}
body = {
     "query": "",
     "gender": "male",
     "weight_kg": 104,
     "height_cm": 182,
     "age": 30
}


def get_result_of_exercise(query: str) -> dict:
    body["query"] = query
    response = requests.post(NUTRIONIX_URL, json=body, headers=headers_nutrix)
    response.raise_for_status()
    body["query"] = ""
    return response.json()["exercises"]


def save_new_workout(workout) -> None:
    response_sheety = requests.post(SHEET_URL, headers=header_sheety, json=workout)
    response_sheety.raise_for_status()


returned_exercises = get_result_of_exercise(input("Tell me again what you did? "))

for exercise in returned_exercises:
    date = datetime.now().strftime("%m/%d/%Y %H:%M:%S").split(" ")
    new_workout = {
        "workout": {
            "date": date[0],
            "time": date[1],
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    save_new_workout(new_workout)

# Deleted all access and used components for security reasons
