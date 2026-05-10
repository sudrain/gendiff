from gen_diff.generate_diff import generate_diff, get_diff_line, get_json


def test_get_json():
    result = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    }
    assert get_json("tests/fixtures/file1.json") == result


def test_get_diff_line():
    res1 = ["   key: value"]
    res2 = [" - key: value"]
    res3 = [" + key: value"]
    res4 = [" - key: old", " + key: new"]
    assert get_diff_line("key", {"key": "value"}, {"key": "value"}) == res1
    assert get_diff_line("key", {"key": "value"}, {"key1": "value"}) == res2
    assert get_diff_line("key", {"key2": "value"}, {"key": "value"}) == res3
    assert get_diff_line("key", {"key": "old"}, {"key": "new"}) == res4


def test_flat_json():
    diff = generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json"
    )
    with open("tests/fixtures/flat_json_result") as f:
        expected = f.read()
    assert diff == expected  # убираем возможный перенос в конце
