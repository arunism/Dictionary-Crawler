import json
import requests
from constant import AUTH_TOKEN


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

endpoint = '/api/v1/Terms/AddNew'
url = 'http://dictionary.arjun.com.np'
endpoint = f'{url}{endpoint}'

response = requests.post(endpoint, data=data, headers=header)
print(response)
# print(response.json())