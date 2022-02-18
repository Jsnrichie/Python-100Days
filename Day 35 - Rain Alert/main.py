import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = 'YOUR SID'
auth_token = 'YOUR TOKEN'

KEY = "YOUR KEY"
MY_LAT = -23.550520 # 26.214661
MY_LONG = -46.633308 #-80.288521
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : KEY,
    "exclude": "minutely,current,daily,alerts"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()
print(weather_data)

hourly_data = weather_data["hourly"][:12] # <---- gets weather data for next 12 hours

will_rain = False

for hour in hourly_data:
    weather_id = hour["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True


if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Bring an umbrella bozo",
        from_='UR TWILIO',
        to='UR ACTUAL NUM'
    )

    print(message.status)
