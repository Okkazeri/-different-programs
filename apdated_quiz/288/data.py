import requests
import json

parameters = {
    "amount": 20,
    "type": "boolean",
}

response = requests.get(
    url="https://opentdb.com/api.php",
    params=parameters
)

data = response.json()
# print(json.dumps(data, indent=4))
question_data = data["results"]
# print(question_data)
