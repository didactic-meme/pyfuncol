import pyfuncol
import pytest

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
    assert [].is_empty() == True


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


def test_fold_left_plus():
    a = l.fold_left(0, lambda acc, n: acc + n)
    assert a == 6


def test_fold_left_concat():
    a = l.fold_left("", lambda acc, n: acc + str(n))
    assert a == "123"


def test_fold_right_plus():
    a = l.fold_right(0, lambda n, acc: acc + n)
    assert a == 6


def test_fold_right_concat():
    a = l.fold_right("", lambda n, acc: acc + str(n))
    assert a == "321"


def test_forall_gt_zero():
    a = l.forall(lambda n: n > 0)
    assert a == True


def test_forall_gt_two():
    a = l.forall(lambda n: n > 2)
    assert a == False


def test_head():
    h = l.head()
    assert h == 1


def test_head_empty():
    l = []
    with pytest.raises(IndexError):
        l.head()


def test_tail():
    t = l.tail()
    assert t == [2, 3]


def test_tail_empty():
    l = []
    with pytest.raises(IndexError):
        l.tail()


def test_take_neg():
    a = l.take(-1)
    assert a == []


def test_take_greater_len():
    a = l.take(4)
    assert a == l


def test_take_smaller_len():
    a = l.take(2)
    assert a == [1, 2]


def test_length():
    a = l.length()
    assert a == 3


def test_length_equal_size():
    assert l.size() == l.length()


# Parallel operations


def test_par_map():
    assert l.par_map(lambda x: x * 2) == [2, 4, 6]
