#-----------------------------------------------------
# 1. requests
import requests
import json

# GET
res = requests.get('http://127.0.0.1:5000')
print(str(res.status_code) + " | " + res.text)

# POST (JSON)
headers = {'Content-Type': 'application/json; chearset=utf-8'}
data = {'title': 'dummy title', 'id': 1, 'message': 'hello world!'}
res = requests.post('http://127.0.0.1:5000', data=json.dumps(data), headers=headers)
print(str(res.status_code) + " | " + res.text)
#-----------------------------------------------------
# 2. urllib
from urllib import request, parse
import json

# GET
req = request.Request('http://127.0.0.1:5000')
res = request.urlopen(req)
print(str(res.status) + " | " + res.read().decode('utf-8'))

# POST (JSON)
headers = {'Content-Type': 'application/json; chearset=utf-8'}
data = {'title': 'dummy title', 'id': 1, 'message': 'hello world!'}
req = request.Request('http://127.0.0.1:5000', headers=headers, data=json.dumps(data).encode('utf-8'))
res = request.urlopen(req)
print(str(res.status) + " | " + res.read().decode('utf-8'))
#-----------------------------------------------------
