import pytest
from day1 import captcha, recaptcha, get_match_index, aoc_input

part1_inputs = [
    ("1122", 3),
    ("1111", 4),
    ("1234", 0),
    ("91212129", 9),
    (aoc_input, 1175)
]

@pytest.mark.parametrize("test_input,expected", part1_inputs)
def test_captcha(test_input, expected):
    assert captcha(test_input) == expected

part2_inputs = [
    ("1212", 6),
    ("1221", 0),
    ("123425", 4),
    ("123123", 12),
    ("12131415", 4),
    (aoc_input, 1166)
]

@pytest.mark.parametrize("test_input,expected", part2_inputs)
def test_recaptcha(test_input, expected):
    assert recaptcha(test_input) == expected

match_index_inputs = [
    (6, 5, 2)
]

@pytest.mark.parametrize("length,current_index,expected", match_index_inputs)
def test_get_match_index(length, current_index, expected):
    assert get_match_index(length, current_index) == expected
