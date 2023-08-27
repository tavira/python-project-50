import pytest

from gendiff.diff.generate_diff import generate_diff

fixture_path = 'tests/fixtures'
fixture_json_path = f'{fixture_path}/json'
fixture_result_path = f'{fixture_path}/result'

empty_json_path = f'{fixture_json_path}/empty.json'
empty_result = f'{fixture_result_path}/empty.txt'
empty_test_case = (empty_json_path, empty_json_path, empty_result)

plain_one_line_json_path = f'{fixture_json_path}/plain_one_line.json'
change_one_line_json_path = f'{fixture_json_path}/changed_one_line.json'
add_one_line_result_path = f'{fixture_result_path}/add_one_line.txt'
add_one_line_test_case = (
    empty_json_path,
    plain_one_line_json_path,
    add_one_line_result_path,
)

remove_one_line_result_path = f'{fixture_result_path}/remove_one_line.txt'
remove_one_line_test_case = (
    plain_one_line_json_path,
    empty_json_path,
    remove_one_line_result_path,
)

unchanged_one_line_result_path = f'{fixture_result_path}/unchange_one_line.txt'
unchanged_one_line_test_case = (
    plain_one_line_json_path,
    plain_one_line_json_path,
    unchanged_one_line_result_path,
)

change_one_line_result_path = f'{fixture_result_path}/change_one_line.txt'
changed_one_line_test_case = (
    plain_one_line_json_path,
    change_one_line_json_path,
    change_one_line_result_path,
)

multiline_before_json_path = f'{fixture_json_path}/multiline_before.json'
multiline_after_json_path = f'{fixture_json_path}/multiline_after.json'
multiline_result_path = f'{fixture_result_path}/multiline.txt'
multiline_test_case = (
    multiline_before_json_path,
    multiline_after_json_path,
    multiline_result_path,
)


@pytest.mark.parametrize(
    'file_before_path,file_after_path,result_path',
    [
        empty_test_case,
        add_one_line_test_case,
        remove_one_line_test_case,
        unchanged_one_line_test_case,
        changed_one_line_test_case,
        multiline_test_case,
    ],
)
def test_plain_json(file_before_path, file_after_path, result_path):
    with open(result_path) as result_file:
        expected = result_file.read()
        actual = generate_diff(file_before_path, file_after_path)
        assert actual == expected
