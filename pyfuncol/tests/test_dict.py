import pyfuncol

d = {"a": 1, "b": 2, "c": 3}


def test_contains():
    assert d.contains("a") == True
    assert d.contains("z") == False


def test_size():
    assert d.size() == 3


def test_filter():
    assert d.filter(lambda kv: kv[1] > 1) == {"b": 2, "c": 3}
