import json
import os

import yaml


def parse(path):
    PARSERS = {
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
        ".json": json.load
    }
    extension = os.path.splitext(path)[1].lower()
    res = PARSERS[extension]((open(path)))
    # print("parse res", res)
    return res
# file1_parsed = parse("tests/fixtures/nested/file1.json")
# file2_parsed = parse("tests/fixtures/nested/file2.json")
