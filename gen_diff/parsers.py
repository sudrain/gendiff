import json

import yaml

parser_keys = {"yaml": yaml.safe_load, "yml": yaml.safe_load, "json": json.load}


def pars_file(path: str):
    *_, end = path.split(".")
    with open(path, "r") as f:
        return parser_keys[end](f)
