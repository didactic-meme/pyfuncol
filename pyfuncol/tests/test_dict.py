import pyfuncol

d = {"a": 1, "b": 2, "c": 3}


def test_contains():
    assert d.contains("a") == True
    assert d.contains("z") == False


def test_size():
    assert d.size() == 3


def test_filter():
    assert d.filter(lambda kv: kv[1] > 1) == {"b": 2, "c": 3}


def test_flat_map():
    assert d.flat_map(lambda kv: {kv[0]: kv[1] ** 2}) == {"a": 1, "b": 4, "c": 9}


def test_foreach():
    tester = []
    d.foreach(lambda kv: tester.append(kv))
    assert tester == [("a", 1), ("b", 2), ("c", 3)]


def test_is_empty():
    assert d.is_empty() == False
    assert {}.is_empty() == True


def test_map():
    assert d.map(lambda kv: (kv[0], kv[1] ** 2)) == {"a": 1, "b": 4, "c": 9}


def test_to_list():
    assert d.to_list() == [("a", 1), ("b", 2), ("c", 3)]

def test_count():
    assert d.count(lambda kv : (kv[0] == "a" or kv[0] == "b") and kv[1] <= 3) == 2
