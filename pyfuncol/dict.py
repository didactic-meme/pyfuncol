from forbiddenfruit import curse
from typing import Callable, Dict, Optional, Tuple, TypeVar, List

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

def fold_left(self: Dict[A, B], z: B, op: Callable[[B, Tuple[A, B]], B]) -> B:
    """
    Applies a binary operator to a start value and all elements of this collection, going left to right.

    Note: will not terminate for infinite-sized collections.

    Note: might return different results for different runs, unless the underlying collection type is ordered or the operator is associative and commutative.

    Args:
        z: the start value.
        op: the binary operator.
    
    Returns:
        the result of inserting op between consecutive elements of this collection, going left to right with the start value z on the left:

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

def filter_not(self: Dict[A, B], p: Callable[[Tuple[A, B]], bool]) -> Dict[A, B]:
    """
    Selects all elements of this iterable collection which do not satisfy a predicate.

    Args: 
        p: The predicate to satisfy.
    
    Returns:
        The filtered dict.
    """
    return {k: v for k, v in self.items() if not p((k, v))}




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
    curse(dict, "fold_left", fold_left)
    curse(dict, "fold_right", fold_right)
    curse(dict, "forall", forall)
    curse(dict, "find", find)
    curse(dict, "filter_not", filter_not)
