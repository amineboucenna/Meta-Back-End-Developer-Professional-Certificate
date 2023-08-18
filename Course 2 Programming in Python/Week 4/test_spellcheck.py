import pytest
import spellcheck as spc

alpha = "Checking the length & structure of the sentence."
# beta = "This sentence should fail the test"

@pytest.fixture
def input_value():
    input = alpha
    return input

def test_length(input_value):
    assert spc.word_count(input_value) < 10
    assert spc.char_count(input_value) < 50
    return None
    raise NotImplementedError()

def test_struc(input_value):
    assert spc.first_char(input_value).isupper()
    assert spc.last_char(input_value) == '.'
    return None
    raise NotImplementedError()

# Run these tests with `python3 -m pytest test_spellcheck.py`
