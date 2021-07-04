from task8 import *
import pytest

@pytest.fixture()
def create_three_positive_ranges():
    return PositiveRange(-100, 500), PositiveRange(22, 30), PositiveRange(1, 100)

def test_create_positive_range():
    r = PositiveRange(-20, 100)
    assert r.begin == -20
    assert r.end == 100

def test_create_positive_range_with_unproper_begin():
    with pytest.raises(NotPositiveRange):
        r = PositiveRange(20, 10)

def test_fibonachi_range_find_index_throigh_vale_method():
    assert FibbonachiRange.find_index_through_value(20) == 8
    assert FibbonachiRange.find_index_through_value(12) == 7

# def test_get_fibbonachi_range(subtests, create_three_positive_ranges):
#     result = [[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], [], [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]]
#     for range in create_three_positive_ranges:
#         with subtests.test(range = range):
#             assert list(range.get_fibbonachi_range()) == result.pop(0)


@pytest.mark.parametrize('result', [[[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], [], [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]]])
def test_get_fibbonachi_range(create_three_positive_ranges, result):
    for range in create_three_positive_ranges:
        assert list(range.get_fibbonachi_range()) == result.pop(0)
