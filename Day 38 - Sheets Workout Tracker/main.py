import requests
import datetime as dt
import os



# ---------------------------------------- NUTRI AI SETUP ---------------------------------------- #
today = dt.datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%X")


APP_ID = os.environ.get("APP_ID")
NUTRI_API = os.environ.get("NUTRI_API")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

ex_params = {
    "query": input("What exercise did you do today?").lower(),
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRI_API,
}

response = requests.post(url=exercise_endpoint, json=ex_params, headers=headers)
exercise_data = response.json()["exercises"]
print(exercise_data)
exercise = exercise_data[0]["name"]
duration = exercise_data[0]["duration_min"]
calories = exercise_data[0]["nf_calories"]




# ---------------------------------------- SHEETY API SETUP ---------------------------------------- #


sheety_endpoint = "https://api.sheety.co/a435b2e3a806ea3f4dc3f634d0796bae/workoutTracking/workouts"

# response = requests.get(url=sheety_endpoint)
# sheet = response.json()
# print(sheet)

post_params = {
    "workout": {
        "date": today_date,
        "time": today_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

headers_sh = {
    "Content-Type": "application/json",
    "Authorization": "Basic anNucmljaDpTcm16ZiFObXUteSVZczlT"
}


response = requests.post(url=sheety_endpoint, json=post_params, headers=headers_sh)




