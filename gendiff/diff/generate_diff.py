import json


def generate_diff(path1, path2):
    with open(path1) as f1, open(path2) as f2:
        content1 = json.loads(f1.read())
        content2 = json.loads(f2.read())

        result = {}
        for key in content2:
            if key not in content1:
                result[key] = {
                    "value": content2[key],
                    "state": "added",
                }
            elif content2[key] != content1[key]:
                result[key] = {
                    "value_before": content1[key],
                    "value_after": content2[key],
                    "state": "changed",
                }
            else:
                result[key] = {
                    "value": content2[key],
                    "state": "unchanged",
                }

        for key in content1:
            if key not in content2:
                result[key] = {
                    "value": content1[key],
                    "state": "deleted",
                }

        result_output = ""
        for key in sorted(result.keys(), key=lambda x: x.lower()):
            if result[key]["state"] == "added":
                result_output += "\n" + \
                    f'  + {key}: {format_value(result[key]["value"])}'
            if result[key]["state"] == "deleted":
                result_output += "\n" + \
                    f'  - {key}: {format_value(result[key]["value"])}'
            if result[key]["state"] == "unchanged":
                result_output += "\n" + \
                    f'    {key}: {format_value(result[key]["value"])}'
            if result[key]["state"] == "changed":
                result_output += "\n" + \
                    f'  - {key}: {format_value(result[key]["value_before"])}' \
                    + "\n" + \
                    f'  + {key}: {format_value(result[key]["value_after"])}'

        wrapped_output = "{\n}\n" \
            if len(result_output) == 0 \
            else "{" + result_output + "\n}\n"

        return wrapped_output


def format_value(value):
    if type(value) == bool:
        return str(value).lower()
    else:
        return value
