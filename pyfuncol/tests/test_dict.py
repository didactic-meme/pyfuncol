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

def test_fold_left():
    assert d.fold_left("", lambda acc, kv: acc + kv[0] + str(kv[1])) == "a1b2c3"

def test_fold_right():
    assert d.fold_right("", lambda kv, acc: acc + kv[0] + str(kv[1])) == "c3b2a1"

def test_forall():
    assert d.forall(lambda kv: kv[1] <= 3) == True

def test_forall_false():
    assert d.forall(lambda kv: kv[1] < 2) == False

def test_find():
    assert d.find(lambda kv: kv[1] == 2) == ("b", 2)

def test_find_none():
    assert d.find(lambda kv: kv[1] == 5) == None
