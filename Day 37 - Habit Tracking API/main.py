import requests
import datetime


USERNAME = "USERNAME"
TOKEN = "TOKEN"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@jsnrich , it is your profile page!","isSuccess":true}


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
print(graph_endpoint+"/"+graph_params["id"])

record_endpoint = f"{graph_endpoint}/{graph_params['id']}"

today = datetime.datetime.now()
today_str = today.strftime("%Y%m%d")

record_params = {
    "date": today_str,
    "quantity": "101"
}

# response = requests.post(url=record_endpoint, json=record_params, headers=headers)
# print(response.text)

update_endpont = f"{record_endpoint}/{today_str}"

update_params = {
    "quantity": "2"
}

# response = requests.put(url=update_endpont, json=update_params, headers=headers)
# print(response.text)

delete_endpoint = update_endpont

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
