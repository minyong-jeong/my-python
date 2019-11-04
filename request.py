import requests
import json

# request (GET)
res = requests.get('http://127.0.0.1:5000')
print(str(res.status_code) + " | " + res.text)

# request (POST - json)
headers = {'Content-Type': 'application/json; chearset=utf-8'}
data = {'title': 'dummy title', 'id': 1, 'message': 'hello world!'}
res = requests.post('http://127.0.0.1:5000', data=json.dumps(data), headers=headers)
print(str(res.status_code) + " | " + res.text)