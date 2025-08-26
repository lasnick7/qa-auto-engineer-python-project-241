import pytest
from gendiff.scripts.gendiff import generate_diff


@pytest.fixture
def files_non_nested():
    return {
        "file1_json": "tests/fixtures/non_nested/file1.json",
        "file2_json": "tests/fixtures/non_nested/file2.json",
        "file1_yaml": "tests/fixtures/non_nested/file1.yaml",
        "file2_yaml": "tests/fixtures/non_nested/file2.yaml",
        "file1_yml": "tests/fixtures/non_nested/file1.yml",
        "file2_yml": "tests/fixtures/non_nested/file2.yml",
    }


@pytest.fixture
def files_nested():
    return {
        "file1_json": "tests/fixtures/nested/file1.json",
        "file2_json": "tests/fixtures/nested/file2.json",
        "file1_yaml": "tests/fixtures/nested/file1.yaml",
        "file2_yaml": "tests/fixtures/nested/file2.yaml",
        "file1_yml": "tests/fixtures/nested/file1.yml",
        "file2_yml": "tests/fixtures/nested/file2.yml",
    }


@pytest.fixture
def non_nested():
    res = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    return res


@pytest.fixture
def nested():
    res = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
    return res


@pytest.fixture
def plain():
    res = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''
    return res


@pytest.fixture
def json_():
    res = '''{
    "common": [
        "nested",
        {
            "follow": [
                "added",
                "false"
            ],
            "setting1": [
                "unchanged",
                "Value 1"
            ],
            "setting2": [
                "deleted",
                "200"
            ],
            "setting3": [
                "changed",
                "true",
                "null"
            ],
            "setting4": [
                "added",
                "blah blah"
            ],
            "setting5": [
                "added",
                {
                    "key5": [
                        "usual",
                        "value5"
                    ]
                }
            ],
            "setting6": [
                "nested",
                {
                    "doge": [
                        "nested",
                        {
                            "wow": [
                                "changed",
                                "",
                                "so much"
                            ]
                        }
                    ],
                    "key": [
                        "unchanged",
                        "value"
                    ],
                    "ops": [
                        "added",
                        "vops"
                    ]
                }
            ]
        }
    ],
    "group1": [
        "nested",
        {
            "baz": [
                "changed",
                "bas",
                "bars"
            ],
            "foo": [
                "unchanged",
                "bar"
            ],
            "nest": [
                "changed",
                {
                    "key": [
                        "usual",
                        "value"
                    ]
                },
                "str"
            ]
        }
    ],
    "group2": [
        "deleted",
        {
            "abc": [
                "usual",
                "12345"
            ],
            "deep": {
                "id": [
                    "usual",
                    "45"
                ]
            }
        }
    ],
    "group3": [
        "added",
        {
            "deep": {
                "id": {
                    "number": [
                        "usual",
                        "45"
                    ]
                }
            },
            "fee": [
                "usual",
                "100500"
            ]
        }
    ]
}'''
    return res


def test_format_stylish_non_nested(files_non_nested, non_nested):
    f = files_non_nested
    assert generate_diff(f["file1_json"], f["file2_json"]) == non_nested
    assert generate_diff(f["file1_yaml"], f["file2_yaml"]) == non_nested
    assert generate_diff(f["file1_yml"], f["file2_yml"]) == non_nested


def test_format_stylish_nested(files_nested, nested):
    f = files_nested
    assert generate_diff(f["file1_json"], f["file2_json"]) == nested
    assert generate_diff(f["file1_yaml"], f["file2_yaml"]) == nested
    assert generate_diff(f["file1_yml"], f["file2_yml"]) == nested


def test_format_plain_nested(files_nested, plain):
    f = files_nested
    assert generate_diff(f["file1_json"], f["file2_json"], "plain") == plain
    assert generate_diff(f["file1_yaml"], f["file2_yaml"], "plain") == plain
    assert generate_diff(f["file1_yml"], f["file2_yml"], "plain") == plain


def test_format_plain_json(files_nested, json_):
    f = files_nested
    assert generate_diff(f["file1_json"], f["file2_json"], "json") == json_
    assert generate_diff(f["file1_yaml"], f["file2_yaml"], "json") == json_
    assert generate_diff(f["file1_yml"], f["file2_yml"], "json") == json_
