import json


def generate_diff(file1, file2):
    data1 = get_json(file1)
    data2 = get_json(file2)
    all_keys = sorted(set(data1.keys() | data2.keys()))
    result = list(map(lambda k: get_diff_line(k, data1, data2), all_keys))
    formated_result = (
        "{\n" + "\n".join(list(map(lambda x: "\n".join(x), result))) + "\n}"  # type: ignore
    )
    return formated_result


def get_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data


def get_diff_line(key, dict1, dict2):
    if key in dict1:
        if key in dict2:
            if dict1[key] != dict2[key]:
                return [f" - {key}: {dict1[key]}", f" + {key}: {dict2[key]}"]
            return [f"   {key}: {dict1[key]}"]
        return [f" - {key}: {dict1[key]}"]
    if key in dict2 and key not in dict1:
        return [f" + {key}: {dict2[key]}"]
