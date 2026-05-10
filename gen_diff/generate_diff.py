import json


def generate_diff(file1, file2):
    data1 = get_json(file1)
    data2 = get_json(file2)
    keys = set(data1.keys() | data2.keys())
    # get_diff_line
    # map(lamda k: get_diff_line(json1, json2), keys)
    pass


def get_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data


def get_diff_line(key, dict1, dict2):
    if key in dict1:
        if key in dict2:
            if dict1[key] != dict2[key]:
                return [f"- {key}: {dict1[key]}", f"+ {key}: {dict2[key]}"]
            return [f"  {key}: {dict1[key]}"]
        return [f"- {key}: {dict1[key]}"]
    if key in dict2 and key not in dict1:
        return [f"+ {key}: {dict2[key]}"]
