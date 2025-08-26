def is_number(s):
    try:
        int(s)  # noqa: F841
        return True
    except Exception:
        return False


def make_line_str(property, option, value=None, from_=None, to_=None):
    ACTIONS = {
        "added": "was added with value:",
        "changed": "was updated.",
        "deleted": "was removed"
    }
    prop = ("Property")

    match option:
        case "added":
            return f"{prop} '{property}' {ACTIONS[option]} {value}"
        case "deleted":
            return f"{prop} '{property}' {ACTIONS[option]}"
        case "changed":
            return f"{prop} '{property}' {ACTIONS[option]} From {from_} to {to_}"  # noqa: E501


def edit_value_str(data):
    no_brackets = {"null", "false", "true"}

    if isinstance(data, dict):
        return '[complex value]'
    elif data in no_brackets or is_number(data):
        return data
    else:
        return f"'{data}'"


def format_plain(diff):
    lines = []

    def build_lines(diff, path=''):
        nonlocal lines
        for k, v in diff.items():
            option, value = v[0], v[1]
            new_path = f"{path}.{k}" if path else k
            match option:
                case "nested":
                    build_lines(value, new_path)
                case "deleted":
                    lines.append(make_line_str(new_path, option))
                case "added":
                    lines.append(make_line_str(new_path, option, value=edit_value_str(value)))  # noqa: E501
                case "changed":
                    v1 = edit_value_str(v[1])
                    v2 = edit_value_str(v[2])
                    lines.append(make_line_str(new_path, option, from_=v1, to_=v2))  # noqa: E501
                case "unchanged":
                    continue

    build_lines(diff)
    res = "\n".join(lines)
    return res
