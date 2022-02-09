from collections import defaultdict
from typing import Callable, Dict, Optional, TypeVar, Set, cast, Iterator
import functools
import dask

A = TypeVar("A")
B = TypeVar("B")
K = TypeVar("K")
U = TypeVar("U")


def map(self: Set[A], f: Callable[[A], B]) -> Set[B]:
    """
    Builds a new set by applying a function to all elements of this set.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new set.
    """
    return cast(Set[B], type(self)(f(x) for x in self))


def filter(self: Set[A], p: Callable[[A], bool]) -> Set[A]:
    """
    Selects all elements of this set which satisfy a predicate.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered set.
    """
    return type(self)(x for x in self if p(x))


def filter_not(self: Set[A], p: Callable[[A], bool]) -> Set[A]:
    """
    Selects all elements of this set which do not satisfy a predicate.

    Args:
        p: The predicate to not satisfy.

    Returns:
        The filtered set.
    """
    return type(self)(x for x in self if not p(x))


def flat_map(self: Set[A], f: Callable[[A], Set[B]]) -> Set[B]:
    """
    Builds a new set by applying a function to all elements of this set and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new set.
    """
    return cast(Set[B], type(self)(y for x in self for y in f(x)))


def contains(self: Set[A], elem: A) -> bool:
    """
    Tests whether this set contains a given value as element.

    Args:
        elem: The element to look for.

    Returns:
        True if the set contains the element, False otherwise.
    """
    return elem in self


def foreach(self: Set[A], f: Callable[[A], U]) -> None:
    """
    Apply f to each element of the set for its side effects.

    Args:
        f: The function to apply to all elements for its side effects.
    """
    for x in self:
        f(x)


def group_by(self: Set[A], f: Callable[[A], K]) -> Dict[K, Set[A]]:
    """
    Partitions this set into a dict of sets according to some discriminator function.

    Args:
        f: The grouping function.

    Returns:
        A dictionary where elements are grouped according to the grouping function.
    """
    # frozenset does not have `add`
    d = defaultdict(set if isinstance(self, frozenset) else type(self))
    for x in self:
        k = f(x)
        d[k].add(x)
    return d


def is_empty(self: Set[A]) -> bool:
    """
    Tests whether the set is empty.

    Returns:
        True if the set is empty, False otherwise.
    """
    return len(self) == 0


def size(self: Set[A]) -> int:
    """
    Computes the size of this set.

    Returns:
        The size of the set.
    """
    return len(self)


def find(self: Set[A], p: Callable[[A], bool]) -> Optional[A]:
    """
    Finds the first element of the set satisfying a predicate, if any.

    Args:
        p: The predicate to satisfy.

    Returns:
        The first element satisfying the predicate, otherwise None.
    """
    for x in self:
        if p(x):
            return x
    return None


def fold_left(self: Set[A], z: B, op: Callable[[B, A], B]) -> B:
    """
    Applies a binary operator to a start value and all elements of this set, going left to right.

    Note: might return different results for different runs, unless the underlying collection type is ordered or the operator is associative and commutative.

    Args:
        z: The start value.
        op: The binary operation.

    Returns:
        The result of inserting op between consecutive elements of this set, going left to right with the start value z on the left:
        op(...op(z, x_1), x_2, ..., x_n)
        where x1, ..., xn are the elements of this set. Returns z if this set is empty.
    """
    acc = z
    for x in self:
        acc = op(acc, x)
    return acc


def fold_right(self: Set[A], z: B, op: Callable[[A, B], B]) -> B:
    """
    Applies a binary operator to all elements of this set and a start value, going right to left.

    Note: might return different results for different runs, unless the underlying collection type is ordered or the operator is associative and commutative.

    Args:
        z: The start value.
        op: The binary operation.

    Returns:
        The result of inserting op between consecutive elements of this set, going right to left with the start value z on the right:
        op(x_1, op(x_2, ... op(x_n, z)...))
        where x1, ..., xn are the elements of this set. Returns z if this set is empty.
    """

    acc = z
    for x in self:
        acc = op(x, acc)
    return acc


def forall(self: Set[A], p: Callable[[A], bool]) -> bool:
    """
    Tests whether a predicate holds for all elements of this set.

    Args:
        p: The predicate used to test elements.

    Returns:
        True if this set is empty or the given predicate p holds for all elements of this set, otherwise False.
    """
    for x in self:
        if not p(x):
            return False

    return True


def length(self: Set[A]) -> int:
    """
    Returns the length (number of elements) of the set. `size` is an alias for length.

    Returns:
        The length of the set
    """
    return len(self)


def to_iterator(self: Set[A]) -> Iterator[A]:
    """
    Converts this set to an iterator.

    Returns:
        An iterator
    """
    return (x for x in self)

# Parallel operations


def par_map(self: Set[A], f: Callable[[A], B]) -> Set[B]:
    """
    Builds a new set by applying in parallel a function to all elements of this set.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new set.
    """
    return cast(Set[B], type(self)((dask.compute(*(dask.delayed(f)(x) for x in self)))))


def par_filter(self: Set[A], p: Callable[[A], bool]) -> Set[A]:
    """
    Selects in parallel all elements of this set which satisfy a predicate.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered set.
    """
    preds = dask.compute(*(dask.delayed(p)(x) for x in self))
    return type(self)(x for i, x in enumerate(self) if preds[i])


def par_filter_not(self: Set[A], p: Callable[[A], bool]) -> Set[A]:
    """
    Selects in parallel all elements of this set which do not satisfy a predicate.

    Args:
        p: The predicate to not satisfy.

    Returns:
        The filtered set.
    """
    preds = dask.compute(*(dask.delayed(p)(x) for x in self))
    return type(self)(x for i, x in enumerate(self) if not preds[i])


def par_flat_map(self: Set[A], f: Callable[[A], Set[B]]) -> Set[B]:
    """
    Builds a new set by applying in parallel a function to all elements of this set and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new set.
    """
    applications = dask.compute(*(dask.delayed(f)(x) for x in self))
    return cast(Set[B], type(self)(x for y in applications for x in y))


# Pure operations


def pure_map(self: Set[A], f: Callable[[A], B]) -> Set[B]:
    """
    Builds a new set by applying a function to all elements of this set using memoization to improve performance.

    WARNING: f must be a PURE function i.e., calling f on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.

    Args:
        f: The PURE function to apply to all elements.

    Returns:
        The new set.
    """
    f_cache = functools.cache(f)
    return cast(Set[B], type(self)(f_cache(x) for x in self))


def pure_flat_map(self: Set[A], f: Callable[[A], Set[B]]) -> Set[B]:
    """
    Builds a new set by applying a function to all elements of this set and using the elements of the resulting collections using memoization to improve performance.

    WARNING: f must be a PURE function i.e., calling f on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new set.
    """
    f_cache = functools.cache(f)
    return cast(Set[B], type(self)(y for x in self for y in f_cache(x)))


def pure_filter(self: Set[A], p: Callable[[A], bool]) -> Set[A]:
    """
    Selects all elements of this set which satisfy a predicate using memoization to improve performance.

    WARNING: p must be a PURE function i.e., calling p on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered set.
    """
    p_cache = functools.cache(p)
    return type(self)(x for x in self if p_cache(x))


def pure_filter_not(self: Set[A], p: Callable[[A], bool]) -> Set[A]:
    """
    Selects all elements of this set which do not satisfy a predicate using memoization to improve performance.

    WARNING: p must be a PURE function i.e., calling p on the same input must always lead to the same result!

    Type A must be hashable using `hash()` function.


    Args:
        p: The predicate not to satisfy.

    Returns:
        The filtered set.
    """
    p_cache = functools.cache(p)
    return type(self)(x for x in self if not p_cache(x))


def lazy_map(self: Set[A], f: Callable[[A], B]) -> Iterator[B]:
    """
    Builds a new set by applying a function to all elements of this set, lazily.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new lazy set, as an iterator.
    """
    for x in self:
        yield f(x)


def lazy_filter(self: Set[A], p: Callable[[A], bool]) -> Iterator[A]:
    """
    Selects all elements of this set which satisfy a predicate, lazily.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered lazy set, as an iterator.
    """
    for x in self:
        if p(x):
            yield x


def lazy_filter_not(self: Set[A], p: Callable[[A], bool]) -> Iterator[A]:
    """
    Selects all elements of this set which do not satisfy a predicate, lazily.

    Args:
        p: The predicate to not satisfy.

    Returns:
        The filtered lazy set, as an iterator.
    """
    for x in self:
        if not p(x):
            yield x


def lazy_flat_map(self: Set[A], f: Callable[[A], Set[B]]) -> Iterator[B]:
    """
    Builds a new lazy set by applying a function to all elements of this set and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new lazy set, as an iterator.
    """
    return (y for x in self for y in f(x))
