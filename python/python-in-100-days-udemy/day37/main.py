import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER = "sadegh"
TOKEN = "dfg54yhtrh335yhgrtg3451"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# POST request to create a user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# POST request to create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "10"
}

# POST request to create a pixel
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "15"
}

# PUT request to update the pixel
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}"

# DELETE request to delete the pixel
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
