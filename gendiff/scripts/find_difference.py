def to_string(data):
    if data is None:
        return "null"
    elif isinstance(data, bool):
        str_data = str(data)
        return f"{str_data[0].lower()}{str_data[1:]}"
    elif isinstance(data, dict):
        res = dict()
        for key in data:
            res[key] = to_string(data[key])
        return res
    return str(data)


def make_usual(dict_):
    res = dict()
    for key in dict_:
        if isinstance(dict_[key], dict):
            value = make_usual(dict_[key])
        else:
            value = ("usual", to_string(dict_[key]))
        res[key] = value
    return res


def find_diff(dict1, dict2):
    added = "added"
    deleted = "deleted"
    changed = "changed"
    unchanged = "unchanged"
    nested = "nested"

    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    ans = dict()

    for key in keys:
        if key in dict1 and key not in dict2:
            ans[key] = (deleted, make_usual(dict1[key])) \
                if isinstance(dict1[key], dict) \
                else (deleted, to_string(dict1[key]))

        elif key not in dict1 and key in dict2:
            if isinstance(dict2[key], dict):
                ans[key] = (added, make_usual(dict2[key]))
            else:
                ans[key] = (added, to_string(dict2[key]))

        elif dict1[key] == dict2[key]:
            if isinstance(dict2[key], dict):
                ans[key] = (unchanged, make_usual(dict2[key]))
            else:
                ans[key] = (unchanged, to_string(dict2[key]))

        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            ans[key] = (nested, find_diff(dict1[key], dict2[key]))
        else:
            if isinstance(dict1[key], dict):
                prev_val = make_usual(dict1[key])
            else:
                prev_val = to_string(dict1[key])

            if isinstance(dict2[key], dict):
                new_val = make_usual(dict2[key])
            else:
                new_val = to_string(dict2[key])

            ans[key] = (changed, prev_val, new_val)

    return ans


# .\.venv\Scripts\python.exe -m gendiff.scripts.find_difference