from gendiff.diff.generate_diff import generate_diff

def test_empty_json():
    with open("tests/fixtures/result/empty.txt") as f:
        expected = f.read()
        actual = generate_diff("tests/fixtures/json/empty.json", "tests/fixtures/json/empty.json")
        assert actual == expected


def test_add_one_line():
    with open("tests/fixtures/result/add_one_line.txt") as f:
        expected = f.read()
        actual = generate_diff("tests/fixtures/json/empty.json", "tests/fixtures/json/plain_one_line.json")
        assert actual == expected


def test_remove_one_line():
    with open("tests/fixtures/result/remove_one_line.txt") as f:
        expected = f.read()
        actual = generate_diff("tests/fixtures/json/plain_one_line.json", "tests/fixtures/json/empty.json")
        assert actual == expected


def test_unchange_one_line():
    with open("tests/fixtures/result/unchange_one_line.txt") as f:
        expected = f.read()
        actual = generate_diff("tests/fixtures/json/plain_one_line.json", "tests/fixtures/json/plain_one_line.json")
        assert actual == expected


def test_change_one_line():
    with open("tests/fixtures/result/change_one_line.txt") as f:
        expected = f.read()
        actual = generate_diff("tests/fixtures/json/plain_one_line.json", "tests/fixtures/json/changed_one_line.json")
        assert actual == expected


def test_plain_multiline():
    with open("tests/fixtures/result/multiline.txt") as f:
        expected = f.read()
        actual = generate_diff("tests/fixtures/json/multiline_before.json", "tests/fixtures/json/multiline_after.json")
        assert actual == expected
