
import requests
import json


url = "http://httpbin.org/post"

data = json.dumps({'key1':'value1','key2':'value2'})
r = requests.post(url, data)

print(r)
print(r.text)
print(r.content)