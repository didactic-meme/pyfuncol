from typing import Callable, Dict, Iterator, Optional, Tuple, TypeVar, List, cast
import functools
import dask

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
D = TypeVar("D")
U = TypeVar("U")


def contains(self: Dict[A, B], key: A) -> bool:
    """
    Tests whether this dict contains a binding for a key.

    Args:
        key: The key to find.

    Returns:
        True if the dict contains a binding for the key, False otherwise.
    """
    return key in self


def size(self: Dict[A, B]) -> int:
    """
    Computes the size of this dict.

    Returns:
        The size of the dict.
    """
    return len(self)


def filter(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> Dict[A, B]:
    """
    Selects all elements of this dict which satisfy a predicate.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered dict.
    """
    return type(self)({k: v for k, v in self.items() if p((k, v))})


def filter_not(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> Dict[A, B]:
    """
    Selects all elements of this dict which do not satisfy a predicate.

    Args:
        p: The predicate to not satisfy.

    Returns:
        The filtered dict.
    """
    return type(self)({k: v for k, v in self.items() if not p((k, v))})


def flat_map(self: Dict[A, B], f: Callable[[Tuple[A, B]], Dict[C, D]]) -> Dict[C, D]:
    """
    Builds a new dict by applying a function to all elements of this dict and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new dict.
    """
    res = cast(Dict[C, D], type(self)())
    for k, v in self.items():
        d = f((k, v))
        res.update(d)
    return res


def foreach(self: Dict[A, B], f: Callable[[Tuple[A, B]], U]) -> None:
    """
    Apply f to each element for its side effects.

    Args:
        f: The function to apply to all elements for its side effects.
    """
    for k, v in self.items():
        f((k, v))


def is_empty(self: Dict[A, B]) -> bool:
    """
    Tests whether the dict is empty.

    Returns:
        True if the dict is empty, False otherwise.
    """
    return len(self) == 0


def map(self: Dict[A, B], f: Callable[[Tuple[A, B]], Tuple[C, D]]) -> Dict[C, D]:
    """
    Builds a new dict by applying a function to all elements of this dict.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new dict.
    """
    return cast(Dict[C, D], type(self)(f(x) for x in self.items()))


def to_list(self: Dict[A, B]) -> List[Tuple[A, B]]:
    """
    Converts this dict to a list of (key, value) pairs.

    Returns:
        A list of pairs corresponding to the entries of the dict
    """
    return [(k, v) for k, v in self.items()]


def to_iterator(self: Dict[A, B]) -> Iterator[Tuple[A, B]]:
    """
    Converts this dict to an iterator of (key, value) pairs.

    Returns:
        An iterator of pairs corresponding to the entries of the dict
    """
    return ((k, v) for k, v in self.items())


def count(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> int:
    """
    Counts the number of elements in the collection which satisfy a predicate.

    Note: will not terminate for infinite-sized collections.

    Args:
        p: The predicate used to test elements.

    Returns:
        The number of elements satisfying the predicate p.
    """
    c = 0
    for t in self.items():
        if p(t):
            c += 1

    return c


def fold_left(self: Dict[A, B], z: B, op: Callable[[B, Tuple[A, B]], B]) -> B:
    """
    Applies a binary operator to a start value and all elements of this collection, going left to right.

    Note: will not terminate for infinite-sized collections.

    Note: might return different results for different runs, unless the underlying collection type is ordered or the operator is associative and commutative.

    Args:
        z: The start value.
        op: The binary operator.

    Returns:
        The result of inserting op between consecutive elements of this collection, going left to right with the start value z on the left:

        op(...op(z, x_1), x_2, ..., x_n)
        where x1, ..., xn are the elements of this collection. Returns z if this collection is empty.
    """
    acc = z
    for t in self.items():
        acc = op(acc, t)

    return acc


def fold_right(self: Dict[A, B], z: B, op: Callable[[Tuple[A, B], B], B]) -> B:
    """
    Applies a binary operator to a start value and all elements of this collection, going right to left.

    Note: will not terminate for infinite-sized collections.

    Note: might return different results for different runs, unless the underlying collection type is ordered or the operator is associative and commutative.

    Args:
        z: The start value.
        op: The binary operator.

    Returns:
        The result of inserting op between consecutive elements of this collection, going right to left with the start value z on the right:

        op(x_1, op(x_2, ... op(x_n, z)...))
        where x1, ..., xn are the elements of this collection. Returns z if this collection is empty.
    """
    acc = z
    for t in reversed(self.items()):
        acc = op(t, acc)

    return acc


def forall(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> bool:
    """
    Tests whether a predicate holds for all elements of this collection.

    Note: may not terminate for infinite-sized collections.

    Args:
        p: The predicate used to test elements.

    Returns:
        True if this collection is empty or the given predicate p holds for all elements of this collection, otherwise False.
    """
    for t in self.items():
        if not p(t):
            return False
    return True


def find(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> Optional[Tuple[A, B]]:
    """
    Finds the first element of the collection satisfying a predicate, if any.

    Note: may not terminate for infinite-sized collections.

    Note: might return different results for different runs, unless the underlying collection type is ordered.

    Args:
        p: The predicate used to test elements.

    Returns:
        An option value containing the first element in the collection that satisfies p, or None if none exists.
    """
    for t in self.items():
        if p(t):
            return t

    return None


# Parallel operations


def par_filter(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> Dict[A, B]:
    """
    Selects in parallel all elements of this dict which satisfy a predicate.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered dict.
    """
    preds = dask.compute(*(dask.delayed(p)(x) for x in self.items()))
    return type(self)({k: v for i, (k, v) in enumerate(self.items()) if preds[i]})


def par_filter_not(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> Dict[A, B]:
    """
    Selects in parallel all elements of this dict which do not satisfy a predicate.

    Args:
        p: The predicate to not satisfy.

    Returns:
        The filtered dict.
    """
    preds = dask.compute(*(dask.delayed(p)(x) for x in self.items()))
    return type(self)({k: v for i, (k, v) in enumerate(self.items()) if not preds[i]})


def par_flat_map(
    self: Dict[A, B], f: Callable[[Tuple[A, B]], Dict[C, D]]
) -> Dict[C, D]:
    """
    Builds a new dict by applying a function in parallel to all elements of this dict and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new dict.
    """
    applications = dask.compute(*(dask.delayed(f)(x) for x in self.items()))
    return cast(
        Dict[C, D], type(self)({k: v for y in applications for k, v in y.items()})
    )


def par_map(self: Dict[A, B], f: Callable[[Tuple[A, B]], Tuple[C, D]]) -> Dict[C, D]:
    """
    Builds a new dict by applying a function in parallel to all elements of this dict.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new dict.
    """
    return cast(
        Dict[C, D],
        type(self)((dask.compute(*(dask.delayed(f)(x) for x in self.items())))),
    )


# Pure operations


def pure_map(self: Dict[A, B], f: Callable[[Tuple[A, B]], Tuple[C, D]]) -> Dict[C, D]:
    """
    Builds a new dict by applying a function to all elements of this dict using memoization to improve performance.

    WARNING: f must be a PURE function i.e., calling f on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new dict.
    """
    f_cache = functools.cache(f)
    return cast(Dict[C, D], type(self)(f_cache(x) for x in self.items()))


def pure_flat_map(
    self: Dict[A, B], f: Callable[[Tuple[A, B]], Dict[C, D]]
) -> Dict[C, D]:
    """
    Builds a new dict by applying a function to all elements of this dict and using the elements of the resulting collections using memoization to improve performance.

    WARNING: f must be a PURE function i.e., calling f on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new dict.
    """
    res = cast(Dict[C, D], type(self)())
    f_cache = functools.cache(f)
    for k, v in self.items():
        d = f_cache((k, v))
        res.update(d)
    return res


def pure_filter(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> Dict[A, B]:
    """
    Selects all elements of this dict which satisfy a predicate using memoization to improve performance.

    WARNING: p must be a PURE function i.e., calling p on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.


    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered dict.
    """
    p_cache = functools.cache(p)
    return type(self)({k: v for k, v in self.items() if p_cache((k, v))})


def pure_filter_not(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> Dict[A, B]:
    """
    Selects all elements of this dict which do not satisfy a predicate using memoization to improve performance.

    WARNING: p must be a PURE function i.e., calling p on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.


    Args:
        p: The predicate not to satisfy.

    Returns:
        The filtered dict.
    """
    p_cache = functools.cache(p)
    return type(self)({k: v for k, v in self.items() if not p_cache((k, v))})


# Lazy operations


def lazy_map(
    self: Dict[A, B], f: Callable[[Tuple[A, B]], Tuple[C, D]]
) -> Iterator[Tuple[C, D]]:
    """
    Builds a new list of tuples by applying a function to all elements of this dict, lazily.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new lazy list of tuples, as an iterator.
    """
    for x in self.items():
        yield f(x)


def lazy_flat_map(
    self: Dict[A, B], f: Callable[[Tuple[A, B]], Dict[C, D]]
) -> Iterator[Tuple[C, D]]:
    """
    Builds a new list of tuples by applying a function to all elements of this dict and using the elements of the resulting collections, lazily.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new lazy list of tuples, as an iterator.
    """
    return (y for x in self.items() for y in f(x).items())


def lazy_filter(
    self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]
) -> Iterator[Tuple[A, B]]:
    """
    Selects all elements of this dict which satisfy a predicate, lazily.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered lazy list of tuples, as an iterator.
    """
    for x in self.items():
        if p(x):
            yield x


def lazy_filter_not(
    self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]
) -> Iterator[Tuple[A, B]]:
    """
    Selects all elements of this dict which do not satisfy a predicate, lazily.

    Args:
        p: The predicate to not satisfy.

    Returns:
        The filtered lazy list of tuples, as an iterator.
    """
    for x in self.items():
        if not p(x):
            yield x
