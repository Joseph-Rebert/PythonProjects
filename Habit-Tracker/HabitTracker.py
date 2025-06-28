import requests
import datetime

TOKEN = "njn32kj4n23jkjknkj432nk"
USERNAME = "wibert"
pixela_endpoint = "https://pixe.la/v1/users"

parameters ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create login info
# response = requests.post(url=pixela_endpoint, json=parameters)

graphs_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

header_parameters = {
    "X-USER-TOKEN": TOKEN
}

graph_parameters = {
    "id": "codelearntrack",
    "name": "Learning Tracker",
    "unit": "time",
    "type": "float",
    "color": "shibafu"
}

# Create new graph
# response = requests.post(url=graphs_endpoint, json=graph_parameters,headers=header_parameters)

pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_parameters["id"]}"
current_day = datetime.datetime.now().date()
current_day = current_day.strftime("%Y%m%d")
pixel_parameters = {
    "date": current_day,
    "quantity": input("How many minutes did you spend learning today?"),
}


response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=header_parameters)

print(response.text)
