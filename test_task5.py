from task5 import *
import pytest
#from pytest_mock import mocker
import sys
from io import StringIO
from unittest import mock
import builtins   

@pytest.fixture()
def create_list_of_functionality():
    return RepresentNumber()

def test_list_of_functionality_language(create_list_of_functionality):
    assert 'Rus' in RepresentNumber.list_of_functionality and  'Eng' in RepresentNumber.list_of_functionality

@pytest.mark.parametrize('range', [[range(0, 100), range(100, 1000), range(1000, 10000), range(10000, 100000), range(100000, 1000000)]])
def test_list_of_functionality_range(create_list_of_functionality, range):
    assert range.pop(0) in RepresentNumber.list_of_functionality['Rus']

def test_valid_possitive_number():
    n = Number('22')
    assert n.abs_number == '22'
    assert n.sign == '+'

def test_valid_negative_number():
    n = Number('-22')
    assert n.abs_number == '22'
    assert n.sign == '-'

def test_unvalid_put_to_number_letters():
    with pytest.raises(NotValiData):
        Number('sda')

def test_unvalid_put_to_number_float_number():
    with pytest.raises(NotValiData):
        Number('1.1')

def test_selector_list_of_functionality(create_list_of_functionality):
    s = Selector('Rus')
    assert s.list_of_functionality == RepresentNumber.list_of_functionality['Rus']

def test_selector_out_of_languages_list_of_functionality(create_list_of_functionality):
    s = Selector('Fr')
    with pytest.raises(TooManyHope):
        s.list_of_functionality 

@pytest.mark.parametrize('number, range', [[11, range(0, 100)], [155, range(100, 1000)], [1200, range(1000, 10000)], [12000, range(10000, 100000)], [999999, range(100000, 1000000)]])
def test_selector_within_range(create_list_of_functionality, number, range):
    s = Selector('Rus')
    assert s.within_range(number) == range

def test_out_of_range_within_range(create_list_of_functionality):
    s = Selector('Rus')
    with pytest.raises(TooManyHope):
        s.within_range(1000000)

@pytest.mark.parametrize('number, string', [['90000', 'девяносто тысячь'], ['44', 'сорок четыре'], ['1000', 'одна тысяча'], ['1001', 'одна тысяча один'],
        ['333333', 'триста тридцать три тысячи триста тридцать три'], ['423563', 'четыреста двадцать три тысячи пятьсот шестьдесят три'], 
        ['151000', 'сто пятьдесят одна тысяча'], ['10252', 'десять тысячь двести пятьдесят два'], ['45310', 'сорок пять тысячь триста десять'],
        ['551001', 'пятьсот пятьдесят одна тысяча один'], ['419002', 'четыреста девятнадцать тысячь два'], ['001', 'один'], ['102872', 'сто две тысячи восемьсот семьдесят два'],
        ['118000', 'сто восемнадцать тысячь'], ['101540', 'сто одна тысяча пятьсот сорок'], ['100511', 'сто тысячь пятьсот одинадцать'],
        ['472084', 'четыреста семьдесят две тысячи восемьдесят четыре'], ['100000', 'сто тысячь'], ['8000', 'восемь тысячь'], 
        ['109', 'сто девять'], ['1111', 'одна тысяча сто одинадцать'], ['987654', 'девятьсот восемьдесят семь тысячь шестьсот пятьдесят четыре'],
        ['110', 'сто десять'], ['21049', 'двадцать одна тысяча сорок девять'], ['93000', 'девяносто три тысячи'], ['612001', 'шестьсот двенадцать тысячь один'], ['0', 'ноль']])
def test_number_string_repr_of_abs_value(create_list_of_functionality, number, string):
    Number.selector = Selector('Rus')
    assert Number(number).string_repr_of_abs_value == string
