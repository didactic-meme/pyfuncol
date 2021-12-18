from forbiddenfruit import curse
from collections import defaultdict
from typing import Callable, Dict, Tuple, TypeVar, List, Union

__A = TypeVar("__A")
__B = TypeVar("__B")
__K = TypeVar("__K")
__U = TypeVar("__U")


def contains(self: Dict[__A, __B], key: __A) -> bool:
    """
    Tests whether this dict contains a binding for a key.
    """
    return key in self


def size(self: Dict[__A, __B]) -> int:
    """
    Computes the size of this dict.
    """
    return len(self)


def filter(
    self: Dict[__A, __B], p: Callable[[Tuple[__A, __B]], bool]
) -> Dict[__A, __B]:
    """
    Selects all elements of this dict which satisfy a predicate.
    """
    return {k: v for k, v in self.items() if p((k, v))}


def curse_dict():
    curse(dict, "contains", contains)
    curse(dict, "size", size)
    curse(dict, "filter", filter)
