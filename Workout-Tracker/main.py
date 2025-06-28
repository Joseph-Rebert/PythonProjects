import requests
import datetime

APP_ID = "a7cf6710"
API_KEY = "0df94623d73e822aedd56d3eb18f1078"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/6bc6217e610f87fa12500bb61497dfbc/myWorkouts/workouts"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_parameters = {
    "query": input("What did you do?")
}


response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_parameters, headers=header)

data = response.json()


payload = {
    "workout":{
        "date": str(datetime.date.today()),
        "time": datetime.datetime.now().strftime("%I:%M:%S %p"),
        "exercise": str(data["exercises"][0]["name"]),
        "duration": str(data["exercises"][0]["duration_min"]),
        "calories": str(data["exercises"][0]["nf_calories"])
    }
}

headers = {
    "Authorization": "nklvnolnouinasdnmxlanlj2"
}

response = requests.post(url=SHEETY_ENDPOINT, json=payload, headers=headers)


