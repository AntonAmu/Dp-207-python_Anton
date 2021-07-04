import pytest
from task7 import Main


@pytest.mark.parametrize('number, result', [(10, '1, 2, 3'), (17, '1, 2, 3, 4'), (16, '1, 2, 3')])
def test_main_get_range_of_natural_numbers(number, result):
    m = Main(number)
    assert m.get_range_of_natural_numbers() == result