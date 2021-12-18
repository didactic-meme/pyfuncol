import pyfuncol

l = [1, 2, 3]


def test_map():
    assert l.map(lambda x: x * 2) == [2, 4, 6]


def test_filter():
    assert l.filter(lambda x: x >= 2) == [2, 3]


def test_flat_map():
    assert l.flat_map(lambda x: [x ** 2]) == [1, 4, 9]


def test_flatten():
    assert [[1, 2], [3]].flatten() == l


def test_contains():
    assert l.contains(2) == True


def test_distinct():
    assert [1, 1, 2, 2, 3].distinct() == l


def test_group_by():
    assert ["abc", "def", "e"].group_by(lambda s: len(s)) == {
        3: ["abc", "def"],
        1: ["e"],
    }


def test_is_empty():
    assert l.is_empty() == False


def test_size():
    assert l.size() == 3


def test_find():
    assert l.find(lambda x: x >= 3) == 3
    assert l.find(lambda x: x < 0) == None


def test_index_of():
    assert l.index_of(3) == 2
    assert l.index_of(42) == -1


def test_foreach():
    tester = []
    l.foreach(lambda x: tester.append(x))
    assert tester == l
