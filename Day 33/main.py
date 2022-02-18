import requests
import datetime as dt

MY_LAT = 51.225808
MY_LONG = -2.341298


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()   # <------ gives exception for particular error
#
# data = response.json()['iss_position']
# print(data)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunrise_time = sunrise.split("T")[1].split("+")[0]
sunset_time = sunset.split("T")[1].split("+")[0]

print(sunrise)
print(sunrise.split("T")[1].split("+")[0])
print(sunrise_time)


now = dt.datetime.now()
print(now)




print(data)

