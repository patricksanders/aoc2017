import pytest
from day2 import *

row_range_input = [
    ([5, 1, 9, 5], 8),
    ([7, 5, 3], 4),
    ([2, 4, 6, 8], 6)
]

@pytest.mark.parametrize("test_input,expected", row_range_input)
def test_get_row_range(test_input, expected):
    assert get_row_range(test_input) == expected


def test_calculate_checksum():
    matrix = [
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8]
    ]
    expected = 18

    assert calculate_checksum(matrix) == expected

def test_part_one():
    expected = 45158
    assert main(filename="input.txt") == expected

row_division_input = [
    ([5, 9, 2, 8], 4),
    ([9, 4, 7, 3], 3),
    ([3, 8, 6, 5], 2)
]

@pytest.mark.parametrize("test_input,expected", row_division_input)
def test_get_row_division(test_input, expected):
    assert get_row_division(test_input) == expected

def test_part_two():
    expected = 294
    assert main(filename="input.txt", use_division=True) == expected
