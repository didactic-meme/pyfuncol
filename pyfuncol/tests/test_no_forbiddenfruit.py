from ..list import *
import pytest

my_list = [1, 2, 3]

def test_map():
    assert map(my_list, lambda x: x * 2) == [2, 4, 6]