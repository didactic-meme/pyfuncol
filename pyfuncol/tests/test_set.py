import pyfuncol

s = {1, 2, 3}
st = frozenset(s)


def test_map():
    assert s.map(lambda x: x * 2) == {2, 4, 6}
    assert st.map(lambda x: x * 2) == frozenset({2, 4, 6})


def test_filter():
    assert s.filter(lambda x: x >= 2) == {2, 3}
    assert st.filter(lambda x: x >= 2) == frozenset({2, 3})


def test_filter_not():
    assert s.filter_not(lambda x: x < 2) == {2, 3}
    assert st.filter_not(lambda x: x < 2) == frozenset({2, 3})


def test_flat_map():
    assert s.flat_map(lambda x: {x ** 2}) == {1, 4, 9}
    assert st.flat_map(lambda x: {x ** 2}) == frozenset({1, 4, 9})


def test_contains():
    assert s.contains(2) == True
    assert st.contains(2) == True


def test_group_by():
    assert {"abc", "def", "e"}.group_by(lambda s: len(s)) == {
        3: {"abc", "def"},
        1: {"e"},
    }
    assert frozenset({"abc", "def", "e"}).group_by(lambda s: len(s)) == {
        3: {"abc", "def"},
        1: {"e"},
    }


def test_is_empty():
    assert s.is_empty() == False
    empty = set()
    assert empty.is_empty() == True

    assert st.is_empty() == False
    frozen_empty = frozenset()
    assert frozen_empty.is_empty() == True


def test_size():
    assert s.size() == 3
    assert st.size() == 3


def test_find():
    assert s.find(lambda x: x >= 3) == 3
    assert s.find(lambda x: x < 0) == None

    assert st.find(lambda x: x >= 3) == 3
    assert st.find(lambda x: x < 0) == None


def test_foreach():
    tester = set()
    s.foreach(lambda x: tester.add(x))
    assert tester == s

    frozen_tester = set()
    st.foreach(lambda x: frozen_tester.add(x))
    assert frozen_tester == s


def test_fold_left_plus():
    assert s.fold_left(0, lambda acc, n: acc + n) == 6
    assert st.fold_left(0, lambda acc, n: acc + n) == 6


def test_fold_left_concat():
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
    assert s.fold_right(0, lambda n, acc: acc + n) == 6
    assert st.fold_right(0, lambda n, acc: acc + n) == 6


def test_fold_right_concat():
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
    assert s.forall(lambda n: n > 0) == True
    assert st.forall(lambda n: n > 0) == True


def test_forall_gt_two():
    assert s.forall(lambda n: n > 2) == False
    assert st.forall(lambda n: n > 2) == False


def test_length():
    assert s.length() == 3
    assert st.length() == 3


def test_length_equal_size():
    assert s.size() == s.length()
    assert st.size() == st.length()


# Parallel operations


def test_par_map():
    assert s.par_map(lambda x: x * 2) == {2, 4, 6}
    assert st.par_map(lambda x: x * 2) == frozenset({2, 4, 6})


def test_par_filter():
    assert s.par_filter(lambda x: x >= 2) == {2, 3}
    assert st.par_filter(lambda x: x >= 2) == frozenset({2, 3})


def test_par_filter_not():
    assert s.par_filter_not(lambda x: x < 2) == {2, 3}
    assert st.par_filter_not(lambda x: x < 2) == frozenset({2, 3})


def test_par_flat_map():
    assert s.par_flat_map(lambda x: [x ** 2]) == {1, 4, 9}
    assert st.par_flat_map(lambda x: {x ** 2}) == frozenset({1, 4, 9})
