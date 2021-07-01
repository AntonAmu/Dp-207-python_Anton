import pytest
from task4 import *
import sys
from unittest import mock

@pytest.fixture()
def text_file(tmpdir):
    a_file = tmpdir.join('text_file.txt')
    a_file.write('Some text for test\nSomething else!')
    return str(Path(a_file))

def test_parse_arg_2_arg_file_not_exists():
    with pytest.raises(FileExistsError):
        args = parse_arg(['test.txt', 'as'])

def test_parse_arg_1_arg_file_exists(text_file):
    with pytest.raises(SystemExit):
        args = parse_arg([text_file])

def test_check_file_exists(text_file):
    assert FileParser.check_file_exists(text_file) == Path(text_file) 

def test_parse_arg_2_arg_file_exists(text_file):
    args = parse_arg([text_file, 'as'])
    assert args.__dict__ == {'file': Path(text_file), 'string_to_find': 'as', 'string_to_replace': None}

def test_parse_arg_3_arg_file_exists(text_file):
    args = parse_arg([text_file, 'as', '-r', 'ss'])
    assert args.__dict__ == {'file': Path(text_file), 'string_to_find': 'as', 'string_to_replace': 'ss'}

def test_find_str_method(text_file):
    fp = FileParser(text_file, 'Some')
    assert fp.find_str() == 'Find 2 strings'


def test_replace_str_method(text_file):
    replaced_text = ['Any text for test\n',  'Anything else!']
    fp = FileParser(text_file, 'Some', 'Any')
    assert fp.replace_str() == 'Replaced 2 strings'
    with open(text_file) as f:
        assert f.readlines() == replaced_text
