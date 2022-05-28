from functions import *

def test_add():
    assert add(2,4) == 6, "Should be 6"
    assert add(2,7) == 9, "Should be 9"

def test_round():
    assert round_plus_ten(4.3) == 14
    assert round_plus_ten(4.7) == 15
    assert round_plus_ten(4.5) == 14