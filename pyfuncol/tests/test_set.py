import pyfuncol
import pytest

s = {1, 2, 3}




def test_map():
    assert s.map(lambda x: x * 2) == {2, 4, 6}


def test_filter():
    assert s.filter(lambda x: x >= 2) == {2, 3}


def test_flat_map():
    assert s.flat_map(lambda x: [x ** 2]) == {1, 4, 9}


def test_contains():
    assert s.contains(2) == True


def test_group_by():
    assert {"abc", "def", "e"}.group_by(lambda s: len(s)) == {
        3: {"abc", "def"},
        1: {"e"},
    }


def test_is_empty():
    assert s.is_empty() == False
    empty = set()
    assert empty.is_empty() == True


def test_size():
    assert s.size() == 3


def test_find():
    assert s.find(lambda x: x >= 3) == 3
    assert s.find(lambda x: x < 0) == None

def test_foreach():
    tester = set()
    s.foreach(lambda x: tester.add(x))
    assert tester == s


def test_fold_left_plus():
    a = s.fold_left(0, lambda acc, n: acc + n)
    assert a == 6


def test_fold_left_concat():
    a = s.fold_left("", lambda acc, n: acc + str(n))
    assert a == "123" or a == "321" or a == "132" or a == "213" or a == "231" or a == "312"


def test_fold_right_plus():
    a = s.fold_right(0, lambda n, acc: acc + n)
    assert a == 6


def test_fold_right_concat():
    a = s.fold_right("", lambda n, acc: acc + str(n))
    assert a == "321" or a == "123" or a == "132" or a == "213" or a == "231" or a == "312"


def test_forall_gt_zero():
    a = s.forall(lambda n: n > 0)
    assert a == True


def test_forall_gt_two():
    a = s.forall(lambda n: n > 2)
    assert a == False

def test_length():
    a = s.length()
    assert a == 3


def test_length_equal_size():
    assert s.size() == s.length()

