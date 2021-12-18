from forbiddenfruit import curse
from collections import defaultdict
from typing import Callable, Dict, TypeVar, List, Union

__A = TypeVar("__A")
__B = TypeVar("__B")
__K = TypeVar("__K")
__U = TypeVar("__U")


def map(self: List[__A], f: Callable[[__A], __B]) -> List[__B]:
    """
    Builds a new list by applying a function to all elements of this list.
    """
    return [f(x) for x in self]


def filter(self: List[__A], p: Callable[[__A], bool]) -> List[__A]:
    """
    Selects all elements of this list which satisfy a predicate.
    """
    return [x for x in self if p(x)]


def flat_map(self: List[__A], f: Callable[[__A], List[__B]]) -> List[__B]:
    """
    Builds a new list by applying a function to all elements of this list and using the elements of the resulting collections.
    """
    return [y for x in self for y in f(x)]


def flatten(self: List[__A]) -> List[__B]:
    """
    Converts this list of lists into a list formed by the elements of these lists.
    """
    return [y for x in self for y in x]


def contains(self: List[__A], elem: __A) -> bool:
    """
    Tests whether this list contains a given value as element
    """
    return elem in self


def distinct(self: List[__A]) -> List[__A]:
    """
    Selects all the elements of this list ignoring the duplicates.
    """
    return list(set(self))


def foreach(self: List[__A], f: Callable[[__A], __U]) -> None:
    """
    Apply f to each element for its side effects.
    """
    [f(x) for x in self]


def group_by(self: List[__A], f: Callable[[__A], __K]) -> Dict[__K, List[__A]]:
    """
    Partitions this list into a map of lists according to some discriminator function.
    """
    d = defaultdict(list)
    for x in self:
        k = f(x)
        d[k].append(x)
    return d


def is_empty(self: List[__A]) -> bool:
    """
    Tests whether the list is empty.
    """
    return len(self) == 0


def size(self: List[__A]) -> int:
    """
    Computes the size of this list.
    """
    return len(self)


def find(self: List[__A], p: Callable[[__A], bool]) -> Union[__A, None]:
    """
    Finds the first element of the list satisfying a predicate, if any.
    """
    for x in self:
        if p(x):
            return x
    return None


def index_of(self: List[__A], elem: __A) -> int:
    """
    Finds index of first occurrence of some value in this list. Returns -1 if non exists.
    """
    for i, x in enumerate(self):
        if x == elem:
            return i
    return -1


def curse_list():
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
