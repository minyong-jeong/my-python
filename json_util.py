import json

def parse_json(json_data):
    """Convert json to dict"""
    dict_data = json.loads(json_data)
    return dict_data

def convert_json(dict_data):
    """Convert dict to json"""
    json_data = json.dumps(dict_data)
    return json_data

if __name__ == "__main__":
    json_data = '{ "p1": { "name": "chulsu", "age": 20 }, "p2": { "name": "younghee", "age": 22 } }'
    result = parse_json(json_data)
    print("parse_json result: %s" % type(result))

    dict_data = { "p1": { "name": "chulsu", "age": 20 }, "p2": { "name": "younghee", "age": 22 } }
    result = convert_json(dict_data)
    print("convert_json result: %s" % type(result))