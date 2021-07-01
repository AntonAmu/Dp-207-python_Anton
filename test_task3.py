import task3
import pytest
from pytest_mock import mocker
import sys
from io import StringIO
from unittest import mock
import builtins   



def test_create_valid_triangles_int_values():
    tr = task3.Triangle('first', '3', '4', '5')
    assert tr.side_1 == 3
    assert tr.side_2 == 4
    assert tr.side_3 == 5
    assert tr.name == 'first'
    assert tr.area == 6
    

def test_create_valid_triangles_float_values():
    tr = task3.Triangle('first', '3', '4.0', '5')
    assert tr.side_1 == 3
    assert tr.side_2 == 4.0
    assert tr.side_3 == 5
    assert tr.name == 'first'
    assert tr.area == 6

@pytest.fixture()
def create_3_valid_tringles():
    tr_1, tr_2, tr_3 =  task3.Triangle('first', '3', '4', '5'), task3.Triangle('second', '6', '8', '10'), task3.Triangle('third', '9', '12', '15')
    return tr_1, tr_2, tr_3

@pytest.fixture()
def create_2_valid_tringles_with_same_name():
    tr_1, tr_2 =  task3.Triangle('first', '3', '4', '5'), task3.Triangle('first', '6', '8', '10')
    return tr_1, tr_2

def test_create_notvalid_triangles_string_values():
    with pytest.raises(task3.ValidationException):
        task3.Triangle('first', '3', 'ass', '5')


def test_create_notvalid_triangles_negative_values():
    with pytest.raises(task3.NotValidinstanceOfTriangleException):
        task3.Triangle('first', '-3', '4', '5')

def test_create_not_triangles_instance_values():
    with pytest.raises(task3.NotValidinstanceOfTriangleException):
        task3.Triangle('first', '3', '4', '55')

def test_comparison_triangle1_less_than_triangle2(create_3_valid_tringles):
    tr_1, tr_2, tr_3 = create_3_valid_tringles
    assert tr_1 < tr_2

def test_comparison_triangle1_greater_than_triangle2(create_3_valid_tringles):
    tr_1, tr_2, tr_3 = create_3_valid_tringles
    assert tr_3 > tr_2

def test_add_tringle_to_list(create_3_valid_tringles):
    tr_1, tr_2, tr_3 = create_3_valid_tringles
    list_ = task3.ListOfTriangles()
    list_.append(tr_1)
    assert list_.list[0] is tr_1 and list_.list[0] == tr_1


def test_create_triangle_from_input():
    input_ = ['first', '3', '4', '5']
    with mock.patch('builtins.input', lambda x: input_.pop(0)):
        tr = task3.create_triangle_from_input() 
        assert tr.side_1 == 3
        assert tr.side_2 == 4
        assert tr.side_3 == 5
        assert tr.name == 'first'
        assert tr.area == 6

def test_add_to_list_triangle_with_same_name_question_to_change_name(create_2_valid_tringles_with_same_name, mocker):
    input_ = ['second']
    task3.answer_choise = mocker.Mock()
    tr_1, tr_2 = create_2_valid_tringles_with_same_name
    list_ = task3.ListOfTriangles()
    list_.append(tr_1)
    with mock.patch('builtins.input', lambda x: input_.pop(0)):
        task3.add_to_list(tr_2, list_)
        task3.answer_choise.assert_called_once_with('Do you want to change name?')


def test_add_to_list_triangle_with_same_name(create_2_valid_tringles_with_same_name, mocker):
    task3.answer_choise = mocker.Mock()
    input_ = ['second']
    task3.answer_choise.side_effect = (True,)
    tr_1, tr_2 = create_2_valid_tringles_with_same_name
    list_ = task3.ListOfTriangles()
    list_.append(tr_1)
    with mock.patch('builtins.input', lambda x: input_.pop(0)):
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            task3.add_to_list(tr_2, list_)
            assert mock_stdout.getvalue() == 'You are trying to add triangle with existed name!\n'
            assert list_.list[1].name == 'second'




def test_list_triangle_str(create_3_valid_tringles):
    list_ = task3.ListOfTriangles()
    for tr in create_3_valid_tringles:
        list_.append(tr)
    assert str(list_) == "===== Triangles list:======\n1. [Triangle first]: 6 cm\n2. [Triangle second]: 24 cm\n3. [Triangle third]: 54 cm\n"


def test_main(mocker):
    answer = [True, True,  False]
    task3.answer_choise = mocker.Mock()
    input_ = ['first', '3', '4', '5', 'second', '6', '8', '10', 'third', '9', '12', '15'] 
    task3.answer_choise.side_effect = (lambda x: answer.pop(0) )
    with mock.patch('builtins.input', lambda x: input_.pop(0)):
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            task3.main()
            assert mock_stdout.getvalue() == "===== Triangles list:======\n1. [Triangle first]: 6 cm\n2. [Triangle second]: 24 cm\n3. [Triangle third]: 54 cm\n\n"
        
