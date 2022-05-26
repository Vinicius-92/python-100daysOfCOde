import requests

params = {
    "amount": 10,
    "type": "boolean"
}
quote_response = requests.get(url="https://opentdb.com/api.php", params=params)
question_data = quote_response.json()["results"]
