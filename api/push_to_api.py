import json
import requests
from constant import AUTH_TOKEN, API_URL, API_ENDPOINT


header = {
    'Authorization': 'Bearer ' + AUTH_TOKEN,
    'content-type': 'application/json'
}


data = {
    "status": 1,
    "languageId": 1,
    "term": "Computer",
    "termClassificationId": 1,
    "origin": "English",
    "definition": "A non-portable computing device",
    "usage": "Let's code on your computer",
    "linkedTermId[]": ""
}

data = json.dumps(data)

endpoint = f'{API_URL}{API_ENDPOINT}'

response = requests.post(endpoint, data=data, headers=header)
print(response)
# print(response.json())