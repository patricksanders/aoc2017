import pytest
from day1 import captcha, aoc_input

inputs = [
    ("1122", 3),
    ("1111", 4),
    ("1234", 0),
    ("91212129", 9),
    (aoc_input, 1175)
]

@pytest.mark.parametrize("test_input,expected", inputs)
def test_captcha(test_input, expected):
    assert captcha(test_input) == expected
