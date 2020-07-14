import pytest
from multi_bracket_validation import __version__
from multi_bracket_validation.multi_bracket_validation import validator

def test_version():
    assert __version__ == '0.1.0'

def test_wiring():
    assert validator

testdata = [
    ("{}", True),
    ("{}(){}", True),
    ("()[[Extra Characters]]", True),
    ("(){}[[]]", True),
    ("{}{Code}[Fellows](())", True),
    ("[({}]", False),
    ("(](", False),
    ("{(})", False),
    ("{]}", False)
]


@pytest.mark.parametrize("input,output", testdata)
def test_case(input,output):
    assert validator(input) == output


