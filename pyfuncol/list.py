from collections import defaultdict
from typing import Callable, Dict, Iterator, Optional, TypeVar, List, cast
import functools
import dask

A = TypeVar("A")
B = TypeVar("B")
K = TypeVar("K")
U = TypeVar("U")


def map(self: List[A], f: Callable[[A], B]) -> List[B]:
    """
    Builds a new list by applying a function to all elements of this list.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new list.
    """
    return cast(List[B], type(self)(f(x) for x in self))


def filter(self: List[A], p: Callable[[A], bool]) -> List[A]:
    """
    Selects all elements of this list which satisfy a predicate.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered list.
    """
    return type(self)(x for x in self if p(x))


def filter_not(self: List[A], p: Callable[[A], bool]) -> List[A]:
    """
    Selects all elements of this list which do not satisfy a predicate.

    Args:
        p: The predicate to not satisfy.

    Returns:
        The filtered list.
    """
    return type(self)(x for x in self if not p(x))


def flat_map(self: List[A], f: Callable[[A], List[B]]) -> List[B]:
    """
    Builds a new list by applying a function to all elements of this list and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new list.
    """
    return cast(List[B], type(self)(y for x in self for y in f(x)))


def flatten(self: List[A]) -> List[B]:
    """
    Converts this list of lists into a list formed by the elements of these lists.

    Returns:
        The flattened list.
    """
    return cast(List[B], type(self)(y for x in self for y in x))


def contains(self: List[A], elem: A) -> bool:
    """
    Tests whether this list contains a given value as element.

    Args:
        elem: The element to look for.

    Returns:
        True if the list contains the element, False otherwise.
    """
    return elem in self


def distinct(self: List[A]) -> List[A]:
    """
    Selects all the elements of this list ignoring the duplicates.

    Returns:
        The list without duplicates.
    """
    return type(self)((set(self)))


def foreach(self: List[A], f: Callable[[A], U]) -> None:
    """
    Apply f to each element for its side effects.

    Args:
        f: The function to apply to all elements for its side effects.
    """
    for x in self:
        f(x)


def group_by(self: List[A], f: Callable[[A], K]) -> Dict[K, List[A]]:
    """
    Partitions this list into a dict of lists according to some discriminator function.

    Args:
        f: The grouping function.

    Returns:
        A dictionary where elements are grouped according to the grouping function.
    """
    d = defaultdict(type(self))
    for x in self:
        k = f(x)
        d[k].append(x)
    return dict(d)


def is_empty(self: List[A]) -> bool:
    """
    Tests whether the list is empty.

    Returns:
        True if the list is empty, False otherwise.
    """
    return len(self) == 0


def size(self: List[A]) -> int:
    """
    Computes the size of this list.

    Returns:
        The size of the list.
    """
    return len(self)


def find(self: List[A], p: Callable[[A], bool]) -> Optional[A]:
    """
    Finds the first element of the list satisfying a predicate, if any.

    Args:
        p: The predicate to satisfy.

    Returns:
        The first element satisfying the predicate, otherwise None.
    """
    for x in self:
        if p(x):
            return x
    return None


def index_of(self: List[A], elem: A) -> int:
    """
    Finds index of first occurrence of some value in this list. Returns -1 if none exists.

    Args:
        elem: The element whose index is to find.

    Returns:
        The index of the first occurrence of the element, or -1 if it does not exists.
    """
    for i, x in enumerate(self):
        if x == elem:
            return i
    return -1


def fold_left(self: List[A], z: B, op: Callable[[B, A], B]) -> B:
    """
    Applies a binary operator to a start value and all elements of this sequence, going left to right.

    Args:
        z: The start value.
        op: The binary operation.

    Returns:
        The result of inserting op between consecutive elements of this sequence, going left to right with the start value z on the left:
        op(...op(z, x_1), x_2, ..., x_n)
        where x1, ..., xn are the elements of this sequence. Returns z if this sequence is empty.
    """
    acc = z
    for x in self:
        acc = op(acc, x)
    return acc


def fold_right(self: List[A], z: B, op: Callable[[A, B], B]) -> B:
    """
    Applies a binary operator to all elements of this list and a start value, going right to left.

    Args:
        z: The start value.
        op: The binary operation.

    Returns:
        The result of inserting op between consecutive elements of this list, going right to left with the start value z on the right:
        op(x_1, op(x_2, ... op(x_n, z)...))
        where x1, ..., xn are the elements of this list. Returns z if this list is empty.
    """

    acc = z
    for x in reversed(self):
        acc = op(x, acc)
    return acc


def forall(self: List[A], p: Callable[[A], bool]) -> bool:
    """
    Tests whether a predicate holds for all elements of this list.

    Args:
        p: The predicate used to test elements.

    Returns:
        True if this list is empty or the given predicate p holds for all elements of this list, otherwise False.
    """
    for x in self:
        if not p(x):
            return False

    return True


def head(self: List[A]) -> A:
    """
    Selects the first element of this iterable collection.

    Note: might return different results for different runs, unless the underlying collection type is ordered.

    Raises:
        IndexError: If the iterable collection is empty.
    """
    if not self:
        raise IndexError()
    return self[0]


def tail(self: List[A]) -> List[A]:
    """
    The rest of the collection without its first element.

    Raises:
        IndexError: If the iterable collection is empty.
    """
    if not self:
        raise IndexError()
    return self[1:]


def take(self: List[A], n: int) -> List[A]:
    """
    Selects the first n elements.

    Args:
        n: The number of elements to take from this list.

    Returns:
        A list consisting only of the first n elements of this list, or else the whole list, if it has less than n elements. If n is negative, returns an empty list.
    """

    if n < 0:
        return type(self)()
    if len(self) <= n:
        return self

    return self[0:n]


def length(self: List[A]) -> int:
    """
    Returns the length (number of elements) of the list. `size` is an alias for length.

    Returns:
        The length of the list
    """
    return len(self)


def to_iterator(self: List[A]) -> Iterator[A]:
    """
    Converts this list to an iterator.

    Returns:
        An iterator
    """
    return (x for x in self)


# Parallel operations


def par_map(self: List[A], f: Callable[[A], B]) -> List[B]:
    """
    Builds a new list by applying a function in parallel to all elements of this list.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new list.
    """
    return cast(
        List[B], type(self)((dask.compute(*(dask.delayed(f)(x) for x in self))))
    )


def par_filter(self: List[A], p: Callable[[A], bool]) -> List[A]:
    """
    Selects in parallel all elements of this list which satisfy a predicate.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered list.
    """
    preds = dask.compute(*(dask.delayed(p)(x) for x in self))
    return type(self)(x for i, x in enumerate(self) if preds[i])


def par_filter_not(self: List[A], p: Callable[[A], bool]) -> List[A]:
    """
    Selects in parallel all elements of this list which do not satisfy a predicate.

    Args:
        p: The predicate to not satisfy.

    Returns:
        The filtered list.
    """
    preds = dask.compute(*(dask.delayed(p)(x) for x in self))
    return type(self)(x for i, x in enumerate(self) if not preds[i])


def par_flat_map(self: List[A], f: Callable[[A], List[B]]) -> List[B]:
    """
    Builds a new list by applying a function in parallel to all elements of this list and using the
    elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new list.
    """
    applications = dask.compute(*(dask.delayed(f)(x) for x in self))
    return cast(List[B], type(self)(z for y in applications for z in y))


def pure_map(self: List[A], f: Callable[[A], B]) -> List[B]:
    """
    Builds a new list by applying a function to all elements of this list using memoization to improve performance.

    WARNING: f must be a PURE function i.e., calling f on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.

    Args:
        f: The PURE function to apply to all elements.

    Returns:
        The new list.
    """
    f_cache = functools.cache(f)
    return cast(List[B], type(self)(f_cache(x) for x in self))


def pure_flat_map(self: List[A], f: Callable[[A], List[B]]) -> List[B]:
    """
    Builds a new list by applying a function to all elements of this list and using the elements of the resulting collections using memoization to improve performance.

    WARNING: f must be a PURE function i.e., calling f on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new list.
    """
    f_cache = functools.cache(f)
    return cast(List[B], type(self)(y for x in self for y in f_cache(x)))


def pure_filter(self: List[A], p: Callable[[A], bool]) -> List[A]:
    """
    Selects all elements of this list which satisfy a predicate using memoization to improve performance.

    WARNING: p must be a PURE function i.e., calling p on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered list.
    """
    p_cache = functools.cache(p)
    return type(self)(x for x in self if p_cache(x))


def pure_filter_not(self: List[A], p: Callable[[A], bool]) -> List[A]:
    """
    Selects all elements of this list which do not satisfy a predicate using memoization to improve performance.

    WARNING: p must be a PURE function i.e., calling p on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.


    Args:
        p: The predicate not to satisfy.

    Returns:
        The filtered list.
    """
    p_cache = functools.cache(p)
    return type(self)(x for x in self if not p_cache(x))


def lazy_map(self: List[A], f: Callable[[A], B]) -> Iterator[B]:
    """
    Builds a new list by applying a function to all elements of this list, lazily.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new lazy list, as an iterator.
    """
    for x in self:
        yield f(x)


def lazy_filter(self: List[A], p: Callable[[A], bool]) -> Iterator[A]:
    """
    Selects all elements of this list which satisfy a predicate, lazily.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered lazy list, as an iterator.
    """
    for x in self:
        if p(x):
            yield x


def lazy_filter_not(self: List[A], p: Callable[[A], bool]) -> Iterator[A]:
    """
    Selects all elements of this list which do not satisfy a predicate, lazily.

    Args:
        p: The predicate to not satisfy.

    Returns:
        The filtered lazy list, as an iterator.
    """
    for x in self:
        if not p(x):
            yield x


def lazy_flat_map(self: List[A], f: Callable[[A], List[B]]) -> Iterator[B]:
    """
    Builds a new lazy list by applying a function to all elements of this list and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new lazy list, as an iterator.
    """
    return (y for x in self for y in f(x))


def lazy_flatten(self: List[A]) -> Iterator[B]:
    """
    Converts this list of lists into a lazy list formed by the elements of these lists.

    Returns:
        The flattened lazy list, as an iterator.
    """
    return (y for x in self for y in x)


def lazy_distinct(self: List[A]) -> Iterator[A]:
    """
    Selects all the elements of this list ignoring the duplicates, lazily.

    Returns:
        The lazy list without duplicates, as an iterator.
    """
    for x in set(self):
        yield x


def lazy_take(self: List[A], n: int) -> Iterator[A]:
    """
    Selects the first n elements, lazily.

    Args:
        n: The number of elements to take from this list.

    Returns:
        A lazy list (as an iterator) consisting only of the first n elements of this list,
        or else the whole lazy list, if it has less than n elements.
        If n is negative, returns an empty lazy list.
    """
    if n < 0:
        yield from ()
    if len(self) <= n:
        for x in self:
            yield x
    else:
        for i in range(n):
            yield self[i]
