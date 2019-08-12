import json

json_data = '{ "p1": { "name": "chulsu", "age": 20 }, "p2": { "name": "younghee", "age": 22 } }'
dict_data = { "p1": { "name": "chulsu", "age": 20 }, "p2": { "name": "younghee", "age": 22 } }

# Convert json to dict
result = json.loads(json_data)  
print("parse_json result: %s" % type(result))

# Convert dict to json
result = json.dumps(dict_data) 
print("convert_json result: %s" % type(result))
