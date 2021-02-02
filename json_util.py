import json


class JsonUtil:
    def convert_json_text_to_dict(self, text):
        return json.loads(text)

    def convert_json_file_to_dict(self, filepath):
        with open(filepath) as f:
            return json.load(f)

    def convert_dict_to_json_text(self, data):
        return json.dumps(data)

    def convert_dict_to_json_file(self, data, filepath):
        with open(filepath, 'w') as f:
            return json.dump(data, f)


json_data = '{"p1": { "name": "A", "age": 20 }, "p2": { "name": "B", "age": 22 }}'
dict_data = {"p1": {"name": "A", "age": 20}, "p2": {"name": "B", "age": 22}}

ju = JsonUtil()
result = ju.convert_json_text_to_dict(json_data)
result = ju.convert_dict_to_json_text(dict_data)

result = ju.convert_json_file_to_dict('./temp/sample.json')
ju.convert_dict_to_json_file(dict_data, './temp/sample2.json')
