from gendiff.diff.build_diff import KeyState


def stringify(diff):
    if not diff:
        return '{\n}'
    alphabetically_sorted_diff_keys = sorted(
        diff.keys(), key=lambda diff_key: diff_key.lower(),
    )
    stringified_diff_items = [
        stringify_diff_item(diff, key)
        for key in alphabetically_sorted_diff_keys
    ]
    return '{{\n{0}\n}}'.format('\n'.join(stringified_diff_items))


def stringify_diff_item(diff, key):
    left_value = _format(diff[key]['left_value'])
    right_value = _format(diff[key]['right_value'])
    state = diff[key]['state']
    match state:
        case KeyState.added:
            return stringify_added_diff_item(key, right_value)
        case KeyState.deleted:
            return stringify_deleted_diff_item(key, left_value)
        case KeyState.unchanged:
            return stringify_unchanged_diff_item(key, left_value)
        case KeyState.changed:
            deletion_line = stringify_deleted_diff_item(key, left_value)
            addition_line = stringify_added_diff_item(key, right_value)
            return f'{deletion_line}\n{addition_line}'


def stringify_added_diff_item(diff_key, diff_value):
    line = _diff_line(diff_key, diff_value)
    return f'  + {line}'


def stringify_deleted_diff_item(diff_key, diff_value):
    line = _diff_line(diff_key, diff_value)
    return f'  - {line}'


def stringify_unchanged_diff_item(diff_key, diff_value):
    line = _diff_line(diff_key, diff_value)
    return f'    {line}'


def _diff_line(diff_key, diff_value):
    return '{key}: {value}'.format(key=diff_key, value=diff_value)


def _format(diff_value):
    if isinstance(diff_value, bool):
        return str(diff_value).lower()
    return diff_value
