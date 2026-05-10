from gen_diff.generate_diff import generate_diff


def test_flat_json():
    diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    with open("tests/fixtures/flat_json_result.json") as f:
        expected = f.read()
    assert diff == expected.strip()  # убираем возможный перенос в конце
