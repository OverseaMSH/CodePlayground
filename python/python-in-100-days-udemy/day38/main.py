import requests
from datetime import datetime

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "male"
WEIGHT_KG = 73
HEIGHT_CM = 167
AGE = 19

# Nutritionix APP ID and API Key from environment variables
APP_ID = "1c6bbb54"  # Your Nutritionix App ID
API_KEY = "07b68bc7a7479522cf2448da1e18e8af"  # Your Nutritionix API Key

# Endpoint for Nutritionix API
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Ask user for exercise input
exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)

# Check if response is successful
if response.status_code == 200:
    result = response.json()
    print(f"Nutritionix API response: \n {result} \n")
else:
    print(f"Error: {response.status_code} - {response.text}")
    exit()

# Get current date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety Project API
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = "https://api.sheety.co/ecf0b60c748fdcc8e729cfa87cba6505/workout/sheet1"  # Sheety endpoint

# Sheety Authentication Details
sheet_username = "sadegh"  # Your Sheety username
sheet_password = "13841384"  # Your Sheety password

# Sheety API Call & Authentication
for exercise in result.get("exercises", []):
    # Create the payload with the correct structure
    sheet_inputs = {
        "sheet1": {  # Replace "sheet1" with your actual sheet name if different
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),  # Ensure this line is included
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Make the API call to Sheety
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(sheet_username, sheet_password)  # Replace with your actual credentials
    )

    # Print the response for debugging
    if sheet_response.status_code == 200:
        print(f"Sheety Response: \n{sheet_response.text}")
    else:
        print(f"Error: {sheet_response.status_code} - {sheet_response.text}")
