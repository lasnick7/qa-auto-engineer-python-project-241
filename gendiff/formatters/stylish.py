SEPARATORS = {
    "unchanged": "  ",
    "added": "+ ",
    "deleted": "- ",
    "tab": "    "
}


def concat_line(option, key, value, level):
    separator = f"{SEPARATORS["tab"] * (level - 1)}{SEPARATORS["unchanged"]}{SEPARATORS[option]}"  # noqa: E501
    return f"{separator}{key}: {value}"


def format_stylish(difference):  # noqa: C901
    lines = []
    open_ = "{"
    close = "}"
    lines.append(open_)

    def build_lines(difference, level=1):
        nonlocal lines
        for k, v in difference.items():
            if len(v) == 1:
                option, value = "usual", v
            else:
                option, value = v[0], v[1]

            match option:
                case "usual":
                    if isinstance(value, dict):
                        lines.append(concat_line("unchanged", k, open_, level))
                        build_lines(value, level + 1)
                    else:
                        lines.append(concat_line("unchanged", k, value, level))

                case "nested":
                    lines.append(concat_line("unchanged", k, open_, level))
                    build_lines(value, level + 1)

                case "changed":
                    value1, value2 = value, v[2]
                    if isinstance(value1, dict):
                        lines.append(concat_line("deleted", k, open_, level))
                        build_lines(value1, level + 1)
                    else:
                        lines.append(concat_line("deleted", k, value1, level))
                    if isinstance(value2, dict):
                        lines.append(concat_line("added", k, open_, level))
                        build_lines(value2, level + 1)
                    else:
                        lines.append(concat_line("added", k, value2, level))

                case _:
                    if isinstance(value, dict):
                        lines.append(concat_line(option, k, open_, level))
                        build_lines(value, level + 1)
                    else:
                        lines.append(concat_line(option, k, value, level))

        lines.append(f"{'    ' * (level - 1)}{close}")

    build_lines(difference)
    res = "\n".join(lines)
    return res
