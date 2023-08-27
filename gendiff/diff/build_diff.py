"""Diff dict between two json objects."""

from enum import Enum


class KeyState(Enum):
    deleted = 'deleted'
    added = 'added'
    changed = 'changed'
    unchanged = 'unchanged'


def build_diff(left, right):
    """
    Generate diff dictionary between two json files.

    :param left: json object (before changes)
    :param right: json object (after changes)
    :return: diff dictionary
    """
    removed_keys = get_removed_keys(left, right)
    added_keys = get_added_keys(left, right)
    keeped_keys = get_keeped_keys(left, right)
    return removed_keys | added_keys | keeped_keys


def get_removed_keys(left, right):
    diff = {}
    deleted_keys = left.keys() - right.keys()
    for key in deleted_keys:
        update_diff(diff, KeyState.deleted, key, left[key], None)
    return diff


def get_added_keys(left, right):
    diff = {}
    added_keys = right.keys() - left.keys()
    for key in added_keys:
        update_diff(diff, KeyState.added, key, None, right[key])
    return diff


def get_keeped_keys(left, right):
    diff = {}
    keeped_keys = left.keys() & right.keys()
    for key in keeped_keys:
        if left[key] == right[key]:
            update_diff(
                diff, KeyState.unchanged, key, left[key], right[key],
            )
        else:
            update_diff(
                diff, KeyState.changed, key, left[key], right[key],
            )
    return diff


def update_diff(diff, state, key, left_value, right_value):
    diff[key] = {
        'state': state,
        'left_value': left_value,
        'right_value': right_value,
    }
