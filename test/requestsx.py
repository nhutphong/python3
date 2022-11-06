import requests
import importlib


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r2 = requests.get('https://httpbin.org/get', params=payload)install