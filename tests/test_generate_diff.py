from gen_diff.generate_diff import (
    generate_diff,
    get_diff_line,
)
from gen_diff.parsers import pars_file


def test_pars_file():
    result = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    }
    assert pars_file("tests/fixtures/file1.yml") == result
    assert pars_file("tests/fixtures/file1.json") == result


def test_get_diff_line():
    res1 = ["   key: value"]
    res2 = [" - key: value"]
    res3 = [" + key: value"]
    res4 = [" - key: old", " + key: new"]
    assert get_diff_line("key", {"key": "value"}, {"key": "value"}) == res1
    assert get_diff_line("key", {"key": "value"}, {"key1": "value"}) == res2
    assert get_diff_line("key", {"key2": "value"}, {"key": "value"}) == res3
    assert get_diff_line("key", {"key": "old"}, {"key": "new"}) == res4


def test_generate_flat_diff():
    diff1 = generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json"
    )
    diff2 = generate_diff(
        "tests/fixtures/file1.yml", "tests/fixtures/file2.yml"
    )
    with open("tests/fixtures/flat_json_result.txt") as f:
        expected = f.read()
    assert diff1 == expected
    assert diff2 == expected
