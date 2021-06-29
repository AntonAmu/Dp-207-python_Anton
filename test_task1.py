import pytest
from task1 import *
import sys
from io import StringIO
from unittest import mock

PERRESENTATION = '* * *\n * * *\n* * *'

def test_str_chessdesk():
    inst = ChessDesk(3, 3)
    assert  inst.__str__() == PERRESENTATION

def test_create_chessdesk():
    inst = ChessDesk(33, 32)
    assert  inst.width == 32
    assert  inst.height == 33

def test_str_chessdesk_1():
    inst = ChessDesk(4, 4)
    assert  inst.__str__() == '* * * *\n * * * *\n* * * *\n * * * *'

def test_parse_arg():
    args = parse_arg(['4', '5'])
    assert args.__dict__ == {'width': 4, 'height': 5}


def test_validation():
    value = validation('2')
    assert value == 2


def test_main():
    with mock.patch.object(sys, 'argv', ['file', '3', '3']):
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            assert mock_stdout.getvalue() == PERRESENTATION + '\n'

@pytest.mark.parametrize("value", ['-2', '2.2'])
def test_validation_raise_error(value):
    with pytest.raises(ValueError):
        value = validation(value)