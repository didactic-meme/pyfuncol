from forbiddenfruit import curse
from collections import defaultdict
from typing import Callable, Dict, Optional, TypeVar, Set
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
    return {f(x) for x in self}


def filter(self: Set[A], p: Callable[[A], bool]) -> Set[A]:
    """
    Selects all elements of this set which satisfy a predicate.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered set.
    """
    return {x for x in self if p(x)}


def flat_map(self: Set[A], f: Callable[[A], Set[B]]) -> Set[B]:
    """
    Builds a new set by applying a function to all elements of this set and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new set.
    """
    return {y for x in self for y in f(x)}


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
    {f(x) for x in self}


def group_by(self: Set[A], f: Callable[[A], K]) -> Dict[K, Set[A]]:
    """
    Partitions this set into a dict of sets according to some discriminator function.

    Args:
        f: The grouping function.

    Returns:
        A dictionary where elements are grouped according to the grouping function.
    """
    d = defaultdict(set)
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


# Parallel operations


def par_map(self: Set[A], f: Callable[[A], B]) -> Set[B]:
    """
    Builds a new set by applying in parallel a function to all elements of this set.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new set.
    """
    return set(dask.compute(*(dask.delayed(f)(x) for x in self)))


def par_filter(self: Set[A], p: Callable[[A], bool]) -> Set[A]:
    """
    Selects in parallel all elements of this set which satisfy a predicate.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered set.
    """
    preds = dask.compute(*(dask.delayed(p)(x) for x in self))
    return {x for i, x in enumerate(self) if preds[i]}


def par_filter_not(self: Set[A], p: Callable[[A], bool]) -> Set[A]:
    """
    Selects in parallel all elements of this set which do not satisfy a predicate.

    Args:
        p: The predicate to not satisfy.

    Returns:
        The filtered set.
    """
    preds = dask.compute(*(dask.delayed(p)(x) for x in self))
    return {x for i, x in enumerate(self) if not preds[i]}


def par_flat_map(self: Set[A], f: Callable[[A], Set[B]]) -> Set[B]:
    """
    Builds a new set by applying in parallel a function to all elements of this set and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new set.
    """
    applications = dask.compute(*(dask.delayed(f)(x) for x in self))
    return {x for y in applications for x in y}


# Pure operations

def pure_map(self: Set[A], f: Callable[[A], B]) -> Set[B]:
    """
    Builds a new set by applying a function to all elements of this set using memoization to improve performance.

    WARNING: f must be a PURE function i.e., calling f on the same input must always lead to the same result!

    type A must be hashable using `hash()` function.

    Args:
        f: The PURE function to apply to all elements.

    Returns:
        The new set.
    """
    res = set()
    f_cache = functools.cache(f)
    for x in self:
        res.add(f_cache(x))
    return res

def pure_flat_map(self: Set[A], f: Callable[[A], Set[B]]) -> Set[B]:
    """
    Builds a new set by applying a function to all elements of this set and using the elements of the resulting collections using memoization to improve performance..

    WARNING: f must be a PURE function i.e., calling f on the same input must always lead to the same result!

    type A must be hashable using `hash()` function.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new set.
    """
    res = set()
    f_cache = functools.cache(f)
    for x in self:
        for y in f_cache(x):
            res.add(y)
    return res



def extend_set():
    """
    Extends the set built-in type with methods.
    """
    curse(set, "map", map)
    curse(set, "filter", filter)
    curse(set, "flat_map", flat_map)
    curse(set, "contains", contains)
    curse(set, "foreach", foreach)
    curse(set, "group_by", group_by)
    curse(set, "is_empty", is_empty)
    curse(set, "size", size)
    curse(set, "find", find)
    curse(set, "fold_left", fold_left)
    curse(set, "fold_right", fold_right)
    curse(set, "forall", forall)
    curse(set, "length", length)

    # Parallel operations
    curse(set, "par_map", par_map)
    curse(set, "par_filter", par_filter)
    curse(set, "par_filter_not", par_filter_not)
    curse(set, "par_flat_map", par_flat_map)

    # Pure operations
    curse(set, "pure_map", par_map)
    curse(set, "pure_flat_map", par_flat_map)