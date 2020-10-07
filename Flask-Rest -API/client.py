import requests


BASE = "http://127.0.0.1:5000/"


response = requests.get(BASE + "video/1")
print(response.json())

data_new = {}
response = requests.put(BASE + "video/1", data_new)

data_updated = {}
response = requests.patch(BASE + "video/1", data_updated)