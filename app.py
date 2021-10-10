import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"

username = "YOUR_USERNAME"
token = "YOUR_SECRET"
graph_id = "CREATE_A_GRAPH_ID"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_params = {
    "id": graph_id,
    "name": "Walking Graph",
    "unit": "kilometer",
    "type": "float",
    "color": "momiji"
}

authenticator = {
    "X-USER-TOKEN": token
}


# response = requests.post(
#     url=graph_endpoint, json=graph_params, headers=authenticator)
# print(response.text)

today = datetime.now()
fmt = "%Y%m%d"
print(today.strftime(fmt))

pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

pixel_params = {
    "date": today.strftime(fmt),
    "quantity": "2.2"
}

# response = requests.post(
#     url=pixel_endpoint, json=pixel_params, headers=authenticator)
# print(response.text)


update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime(fmt)}"
update_params = {
    "quantity": "3.5"
}

# response = requests.put(url=update_endpoint,
#                         json=update_params, headers=authenticator)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime(fmt)}"
response = requests.delete(url=delete_endpoint, headers=authenticator)
print(response.text)
