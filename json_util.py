import json

class JsonUtil:

    def parse_json(self, json_data):
        dict_data = json.loads(json_data)
        return dict_data

    def convert_json(self, dict_data):
        json_data = json.dumps(dict_data)
        return json_data

if __name__ == "__main__":
    ju = JsonUtil()
    json_data = '{ "p1": { "name": "chulsu", "age": "20" }, "p2": { "name": "younghee", "age": "22" } }'
    dict_data = { "p1": { "name": "chulsu", "age": 20 }, "p2": { "name": "younghee", "age": 22 } }
    print(ju.parse_json(json_data))
    print(ju.convert_json(dict_data))