from .. import dict as pfcdict
from .. import list as pfclist
from .. import set as pfcset

def test_dict():
    assert pfcdict.map({'a': 1, 'b': 2, 'c': 3}, lambda x: (x[0], x[1] * 2)) == {'a': 2, 'b': 4, 'c': 6}

def test_list():
    assert pfclist.map([1, 2, 3], lambda x: x * 2) == [2, 4, 6]

def test_set():
    assert pfcset.map({1, 2, 3}, lambda x: x * 2) == {2, 4, 6}