from forbiddenfruit import curse
from collections import defaultdict
from typing import Callable, Dict, Optional, TypeVar, List

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
    return [f(x) for x in self]


def filter(self: List[A], p: Callable[[A], bool]) -> List[A]:
    """
    Selects all elements of this list which satisfy a predicate.

    Args:
        p: The predicate to satisfy.

    Returns:
        The filtered list.
    """
    return [x for x in self if p(x)]


def flat_map(self: List[A], f: Callable[[A], List[B]]) -> List[B]:
    """
    Builds a new list by applying a function to all elements of this list and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new list.
    """
    return [y for x in self for y in f(x)]


def flatten(self: List[A]) -> List[B]:
    """
    Converts this list of lists into a list formed by the elements of these lists.

    Returns:
        The flattened list.
    """
    return [y for x in self for y in x]


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
    return list(set(self))


def foreach(self: List[A], f: Callable[[A], U]) -> None:
    """
    Apply f to each element for its side effects.

    Args:
        f: The function to apply to all elements for its side effects.
    """
    [f(x) for x in self]


def group_by(self: List[A], f: Callable[[A], K]) -> Dict[K, List[A]]:
    """
    Partitions this list into a dict of lists according to some discriminator function.

    Args:
        f: The grouping function.

    Returns:
        A dictionary where elements are grouped according to the grouping function.
    """
    d = defaultdict(list)
    for x in self:
        k = f(x)
        d[k].append(x)
    return d


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
        z: start value
        op: binary operation

    Returns:
        the result of inserting op between consecutive elements of this sequence, going left to right with the start value z on the left:
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
        z: start value
        op: binary operation

    Returns:
        the result of inserting op between consecutive elements of this list, going right to left with the start value z on the right:
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
        p: the predicate used to test elements.
        returns: true if this list is empty or the given predicate p holds for all elements of this list, otherwise false.
    """
    for x in self:
        if not p(x):
            return False
    
    return True

def head(self: List[A]) -> A:
    """
    Selects the first element of this iterable collection.

    Note: might return different results for different runs, unless the underlying collection type is ordered.

    Exceptions thrown:
        IndexError if the iterable collection is empty.
    """
    if not self:
        raise IndexError()
    return self[0]

def tail(self: List[A]) -> List[A]:
    """
    The rest of the collection without its first element.

    Exceptions thrown:
        IndexError if the iterable collection is empty.
    """
    if not self:
        raise IndexError()
    return self[1:]

def extend_list():
    """
    Extends the list built-in type with methods.
    """
    curse(list, "map", map)
    curse(list, "filter", filter)
    curse(list, "flat_map", flat_map)
    curse(list, "flatten", flatten)
    curse(list, "contains", contains)
    curse(list, "distinct", distinct)
    curse(list, "foreach", foreach)
    curse(list, "group_by", group_by)
    curse(list, "is_empty", is_empty)
    curse(list, "size", size)
    curse(list, "find", find)
    curse(list, "index_of", index_of)
    curse(list, "fold_left", fold_left)
    curse(list, "fold_right", fold_right)
    curse(list, "forall", forall)
    curse(list, "head", head)
    curse(list, "tail", tail)
