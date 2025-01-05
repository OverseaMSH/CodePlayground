import requests

API_KEY = "4602ff2110cde5610d233e765d813257"
ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    "lat": 35.6892,   # Tehran latitude
    "lon": 51.3890,   # Tehran longitude
    "appid": API_KEY,
}

response = requests.get(url=ENDPOINT, params=parameters)

if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)
