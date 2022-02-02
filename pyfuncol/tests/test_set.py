from operator import ne
import pyfuncol

s = {1, 2, 3}
st = frozenset(s)


def test_map():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.map(lambda x: x * 2) == {2, 4, 6}
    assert st.map(lambda x: x * 2) == frozenset({2, 4, 6})


def test_filter():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.filter(lambda x: x >= 2) == {2, 3}
    assert st.filter(lambda x: x >= 2) == frozenset({2, 3})


def test_filter_not():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.filter_not(lambda x: x < 2) == {2, 3}
    assert st.filter_not(lambda x: x < 2) == frozenset({2, 3})


def test_flat_map():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.flat_map(lambda x: {x**2}) == {1, 4, 9}
    assert st.flat_map(lambda x: {x**2}) == frozenset({1, 4, 9})


def test_contains():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.contains(2) == True
    assert st.contains(2) == True


def test_group_by():
    s = {1, 2, 3}
    st = frozenset(s)
    assert {"abc", "def", "e"}.group_by(lambda s: len(s)) == {
        3: {"abc", "def"},
        1: {"e"},
    }
    assert frozenset({"abc", "def", "e"}).group_by(lambda s: len(s)) == {
        3: {"abc", "def"},
        1: {"e"},
    }


def test_is_empty():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.is_empty() == False
    empty = set()
    assert empty.is_empty() == True

    assert st.is_empty() == False
    frozen_empty = frozenset()
    assert frozen_empty.is_empty() == True


def test_size():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.size() == 3
    assert st.size() == 3


def test_find():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.find(lambda x: x >= 3) == 3
    assert s.find(lambda x: x < 0) == None

    assert st.find(lambda x: x >= 3) == 3
    assert st.find(lambda x: x < 0) == None


def test_foreach():
    s = {1, 2, 3}
    st = frozenset(s)
    tester = set()
    s.foreach(lambda x: tester.add(x))
    assert tester == s

    frozen_tester = set()
    st.foreach(lambda x: frozen_tester.add(x))
    assert frozen_tester == s


def test_fold_left_plus():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.fold_left(0, lambda acc, n: acc + n) == 6
    assert st.fold_left(0, lambda acc, n: acc + n) == 6


def test_fold_left_concat():
    s = {1, 2, 3}
    st = frozenset(s)
    a = s.fold_left("", lambda acc, n: acc + str(n))
    assert (
        a == "123" or a == "321" or a == "132" or a == "213" or a == "231" or a == "312"
    )

    frozen_a = st.fold_left("", lambda acc, n: acc + str(n))
    assert (
        frozen_a == "123"
        or frozen_a == "321"
        or frozen_a == "132"
        or frozen_a == "213"
        or frozen_a == "231"
        or frozen_a == "312"
    )


def test_fold_right_plus():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.fold_right(0, lambda n, acc: acc + n) == 6
    assert st.fold_right(0, lambda n, acc: acc + n) == 6


def test_fold_right_concat():
    s = {1, 2, 3}
    st = frozenset(s)
    a = s.fold_right("", lambda n, acc: acc + str(n))
    assert (
        a == "321" or a == "123" or a == "132" or a == "213" or a == "231" or a == "312"
    )

    frozen_a = st.fold_right("", lambda n, acc: acc + str(n))
    assert (
        frozen_a == "321"
        or frozen_a == "123"
        or frozen_a == "132"
        or frozen_a == "213"
        or frozen_a == "231"
        or frozen_a == "312"
    )


def test_forall_gt_zero():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.forall(lambda n: n > 0) == True
    assert st.forall(lambda n: n > 0) == True


def test_forall_gt_two():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.forall(lambda n: n > 2) == False
    assert st.forall(lambda n: n > 2) == False


def test_length():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.length() == 3
    assert st.length() == 3


def test_length_equal_size():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.size() == s.length()
    assert st.size() == st.length()


def test_to_iterator():
    s = {1, 2, 3}
    st = frozenset(s)
    sbis = s.copy()

    it = s.to_iterator()
    sit = st.to_iterator()

    n = next(it)
    ns = next(sit)
    assert n in s
    assert ns in st

    remaining = set(it)
    remainings = set(sit)
    s.remove(n)
    sbis.remove(ns)
    assert remaining == s
    assert remainings == sbis


# Parallel operations


def test_par_map():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.par_map(lambda x: x * 2) == {2, 4, 6}
    assert st.par_map(lambda x: x * 2) == frozenset({2, 4, 6})


def test_par_filter():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.par_filter(lambda x: x >= 2) == {2, 3}
    assert st.par_filter(lambda x: x >= 2) == frozenset({2, 3})


def test_par_filter_not():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.par_filter_not(lambda x: x < 2) == {2, 3}
    assert st.par_filter_not(lambda x: x < 2) == frozenset({2, 3})


def test_par_flat_map():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.par_flat_map(lambda x: [x**2]) == {1, 4, 9}
    assert st.par_flat_map(lambda x: {x**2}) == frozenset({1, 4, 9})


# Pure operations


def test_pure_map():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.pure_map(lambda x: x * 2) == {2, 4, 6}
    assert st.pure_map(lambda x: x * 2) == {2, 4, 6}


def test_pure_flat_map():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.pure_flat_map(lambda x: [x**2]) == {1, 4, 9}
    assert st.pure_flat_map(lambda x: [x**2]) == {1, 4, 9}


def test_pure_filter():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.pure_filter(lambda x: x >= 2) == {2, 3}
    assert st.pure_filter(lambda x: x >= 2) == {2, 3}


def test_pure_filter_not():
    s = {1, 2, 3}
    st = frozenset(s)
    assert s.pure_filter_not(lambda x: x >= 2) == {1}
    assert st.pure_filter_not(lambda x: x >= 2) == {1}


# Lazy operations


def test_lazy_map():
    s = {1, 2, 3}
    st = frozenset(s)
    res = s.lazy_map(lambda x: x * 2)

    assert next(res) == 2
    assert set(res) == {4, 6}


def test_lazy_flat_map():
    s = {1, 2, 3}
    st = frozenset(s)
    res = s.lazy_flat_map(lambda x: [x * 2])

    assert next(res) == 2
    assert set(res) == {4, 6}


def test_lazy_filter():
    s = {1, 2, 3}
    st = frozenset(s)
    res = s.lazy_filter(lambda x: x >= 2)

    assert next(res) == 2
    assert set(res) == {3}


def test_lazy_filter_not():
    s = {1, 2, 3}
    st = frozenset(s)
    res = s.lazy_filter_not(lambda x: x < 2)
    assert next(res) == 2
    assert set(res) == {3}
