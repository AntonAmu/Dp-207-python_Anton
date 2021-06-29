import task2
import pytest
import sys
from io import StringIO
from unittest import mock
import builtins   


@pytest.fixture()
def create_2_valid_envelop_to_negative():
    env_1, env_2 =  task2.Envelope('2', '2'), task2.Envelope('2', '2')
    return env_1, env_2

@pytest.fixture()
def create_2_valid_envelop():
    env_1, env_2 = task2.Envelope('2', '2'), task2.Envelope('3', '3')
    return env_1, env_2


@pytest.mark.parametrize("side_1, side_2", [('-2', '2'), ('ds', '-2')])
def test_invalid_envelop(side_1, side_2):
    with pytest.raises(task2.ValidationException):
        task2.Envelope(side_1, side_2)

def test_create_valid_float_envelop():
    env = task2.Envelope('2.0', '2.2')
    assert env.side_1 == 2
    assert env.side_2 == 2.2

def test_positive_put_in_envelopes(create_2_valid_envelop):
    env_1, env_2 = create_2_valid_envelop
    assert env_1.put_in_envelope(env_2) == "You can put in each other"

def test_negative_put_in_envelopes(create_2_valid_envelop_to_negative):
    env_1, env_2 = create_2_valid_envelop_to_negative
    assert env_1.put_in_envelope(env_2) == "You can not put in each other"

@pytest.mark.parametrize("question, from_user, response, output", [('Try again?', ['y'], True, ""), ('Try again?', ['n'], False, ""),
                                                                    ('Try again?', ['some', 'y'], True, "We couldn't understand you\n")])
def test_answer(question, from_user, response, output):
    with mock.patch('builtins.input', lambda x: from_user.pop(0)):
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            assert task2.answer_choise(question) == response
            assert mock_stdout.getvalue() == output

