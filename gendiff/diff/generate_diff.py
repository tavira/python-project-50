"""Diff generation between two json files."""
import json

from gendiff.diff.build_diff import build_diff
from gendiff.diff.stringify_diff import stringify


def generate_diff(path1, path2):
    """
    Generate diff string between two json files.

    :param path1: path to json file(diff left side)
    :param path2: path to json file(diff right side)
    :return: diff as string
    """
    with open(path1) as fd1:
        with open(path2) as fd2:
            left_content = json.loads(fd1.read())
            right_content = json.loads(fd2.read())
            diff = build_diff(left_content, right_content)
            return stringify(diff)
