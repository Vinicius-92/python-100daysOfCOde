from datetime import datetime
import requests

USERNAME = "vinicius92as"
TOKEN = "listentoyourhear"

pixela_url = "https://pixe.la/v1/users"
user_params = {
    "token": "listentoyourhear",
    "username": "vinicius92as",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Created user
# response = requests.post(url=pixela_url, json=user_params)

graph_endpoint = f"{pixela_url}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# Creating a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = datetime.now().strftime("%Y%m%d")
body_create_data = {
    "date": today,
    "quantity": "1"
}
posting_value_endpoint = f"{pixela_url}/{USERNAME}/graphs/graph1"

# Add values to graph
# response = requests.post(url=posting_value_endpoint, headers=headers, json=body_data)

body_update_data = {
    "quantity": "20"
}
updating_value_endpoint = f"{pixela_url}/{USERNAME}/graphs/graph1/{today}"

# Updating pixel value
# response = requests.put(url=updating_value_endpoint, headers=headers, json=body_update_data)

deleting_value_endpoint = f"{pixela_url}/{USERNAME}/graphs/graph1/{today}"
response = requests.delete(url=deleting_value_endpoint, headers=headers)
print(response.text)
