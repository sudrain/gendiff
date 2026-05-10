from gen_diff.parsers import pars_file


def generate_diff(file1, file2):
    data1 = pars_file(file1)
    data2 = pars_file(file2)
    all_keys = sorted(set(data1.keys() | data2.keys()))
    result = list(map(lambda k: get_diff_line(k, data1, data2), all_keys))
    formated_result = (
        "{\n" + "\n".join(list(map(lambda x: "\n".join(x), result))) + "\n}"  # type: ignore
    )
    return formated_result


def get_diff_line(key, dict1, dict2):
    if key in dict1:
        if key in dict2:
            if dict1[key] != dict2[key]:
                return [
                    f" - {key}: {format_value(dict1[key])}",
                    f" + {key}: {format_value(dict2[key])}",
                ]
            return [f"   {key}: {format_value(dict1[key])}"]
        return [f" - {key}: {format_value(dict1[key])}"]
    if key in dict2:
        return [f" + {key}: {format_value(dict2[key])}"]


def format_value(val):
    return str(val).lower()
