from forbiddenfruit import curse
from typing import Callable, Dict, Tuple, TypeVar, List

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
    return {k: v for k, v in self.items() if p((k, v))}


def flat_map(self: Dict[A, B], f: Callable[[Tuple[A, B]], Dict[C, D]]) -> Dict[C, D]:
    """
    Builds a new dict by applying a function to all elements of this dict and using the elements of the resulting collections.

    Args:
        f: The function to apply to all elements.

    Returns:
        The new dict.
    """
    res = {}
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
    [f((k, v)) for k, v in self.items()]


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
    res = {}
    for k, v in self.items():
        k1, v1 = f((k, v))
        res[k1] = v1
    return res


def to_list(self: Dict[A, B]) -> List[Tuple[A, B]]:
    """
    Converts this dict to a list of (key, value) pairs.

    Returns:
        A list of pairs corresponding to the entries of the dict
    """
    return [(k, v) for k, v in self.items()]

def count(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> int:
    """
    Counts the number of elements in the collection which satisfy a predicate.

    Note: will not terminate for infinite-sized collections.

    Args:
        p: the predicate used to test elements.
    
    Returns:
        the number of elements satisfying the predicate p.
    """
    c = 0
    for t in self.items():
        if p(t):
            c += 1
    
    return c


def extend_dict():
    """
    Extends the dict built-in type with methods.
    """
    curse(dict, "contains", contains)
    curse(dict, "size", size)
    curse(dict, "filter", filter)
    curse(dict, "flat_map", flat_map)
    curse(dict, "foreach", foreach)
    curse(dict, "is_empty", is_empty)
    curse(dict, "map", map)
    curse(dict, "to_list", to_list)
    curse(dict, "count", count)
