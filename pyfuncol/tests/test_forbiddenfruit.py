import pyfuncol
import pytest

my_list = [1, 2, 3]

def test_map():
    assert my_list.map(lambda x: x * 2) == [2, 4, 6]