import requests

quote_response = requests.get(url="https://api.kanye.rest/")
print(quote_response.json()["quote"])
