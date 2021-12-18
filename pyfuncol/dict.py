from forbiddenfruit import curse
from typing import Callable, Dict, Tuple, TypeVar, List

__A = TypeVar("__A")
__B = TypeVar("__B")
__C = TypeVar("__C")
__D = TypeVar("__D")
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


def flat_map(
    self: Dict[__A, __B], f: Callable[[Tuple[__A, __B]], Dict[__C, __D]]
) -> Dict[__C, __D]:
    """
    Builds a new dict by applying a function to all elements of this dict and using the elements of the resulting collections.
    """
    res = {}
    for k, v in self.items():
        d = f((k, v))
        res.update(d)
    return res


def foreach(self: Dict[__A, __B], f: Callable[[Tuple[__A, __B]], __U]) -> None:
    """
    Apply f to each element for its side effects.
    """
    [f((k, v)) for k, v in self.items()]


def is_empty(self: Dict[__A, __B]) -> bool:
    """
    Tests whether the dict is empty.
    """
    return len(self) == 0


def map(
    self: Dict[__A, __B], f: Callable[[Tuple[__A, __B]], Tuple[__C, __D]]
) -> Dict[__C, __D]:
    """
    Builds a new dict by applying a function to all elements of this dict.
    """
    res = {}
    for k, v in self.items():
        k1, v1 = f((k, v))
        res[k1] = v1
    return res


def to_list(self: Dict[__A, __B]) -> List[Tuple[__A, __B]]:
    return [(k, v) for k, v in self.items()]


def curse_dict():
    curse(dict, "contains", contains)
    curse(dict, "size", size)
    curse(dict, "filter", filter)
    curse(dict, "flat_map", flat_map)
    curse(dict, "foreach", foreach)
    curse(dict, "is_empty", is_empty)
    curse(dict, "map", map)
    curse(dict, "to_list", to_list)
