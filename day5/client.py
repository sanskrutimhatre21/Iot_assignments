import requests
import json

url = "http://172.18.7.31:4000/add"
data = {
  "name":"python",
  "age":40,
  "city":"pune",
  "steps":1500,
  "pulse":92,
  "oxygen":94,
  "temperature":98.0
}
# import requests
# import json

# url = "http://172.18.7.31:4000/all"

# responseCode = requests.get(url)
# print(responseCode)
# info = json.loads(responseCode.content)
# print(info)

# response = requests.post(url, json=data, headers={"content-type":"Application/JSON"})
# print(response)
# print(response.content)