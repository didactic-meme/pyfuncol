from warnings import warn

from . import dict as pfcdict
from . import list as pfclist
from . import set as pfcset

EXTEND_BUILTINS = False
try:
    from forbiddenfruit import curse

    EXTEND_BUILTINS = True
except ImportError:
    warn(
        "[WARNING] You are using pyfuncol without forbiddenfruit. Functions will not extend builtins"
    )


def extend_dict():
    """
    Extends the dict built-in type with methods.
    """
    curse(dict, "contains", pfcdict.contains)
    curse(dict, "size", pfcdict.size)
    curse(dict, "filter", pfcdict.filter)
    curse(dict, "filter_not", pfcdict.filter_not)
    curse(dict, "flat_map", pfcdict.flat_map)
    curse(dict, "foreach", pfcdict.foreach)
    curse(dict, "is_empty", pfcdict.is_empty)
    curse(dict, "map", pfcdict.map)
    curse(dict, "to_list", pfcdict.to_list)
    curse(dict, "to_iterator", pfcdict.to_iterator)
    curse(dict, "count", pfcdict.count)
    curse(dict, "fold_left", pfcdict.fold_left)
    curse(dict, "fold_right", pfcdict.fold_right)
    curse(dict, "forall", pfcdict.forall)
    curse(dict, "find", pfcdict.find)

    # Parallel operations
    curse(dict, "par_map", pfcdict.par_map)
    curse(dict, "par_filter", pfcdict.par_filter)
    curse(dict, "par_filter_not", pfcdict.par_filter_not)
    curse(dict, "par_flat_map", pfcdict.par_flat_map)

    # Pure operations
    curse(dict, "pure_map", pfcdict.pure_map)
    curse(dict, "pure_flat_map", pfcdict.pure_flat_map)
    curse(dict, "pure_filter", pfcdict.pure_filter)
    curse(dict, "pure_filter_not", pfcdict.pure_filter_not)

    # Lazy operations
    curse(dict, "lazy_map", pfcdict.lazy_map)
    curse(dict, "lazy_flat_map", pfcdict.lazy_flat_map)
    curse(dict, "lazy_filter", pfcdict.lazy_filter)
    curse(dict, "lazy_filter_not", pfcdict.lazy_filter_not)


def extend_list():
    """
    Extends the list built-in type with methods.
    """
    curse(list, "map", pfclist.map)
    curse(list, "filter", pfclist.filter)
    curse(list, "filter_not", pfclist.filter_not)
    curse(list, "flat_map", pfclist.flat_map)
    curse(list, "flatten", pfclist.flatten)
    curse(list, "contains", pfclist.contains)
    curse(list, "distinct", pfclist.distinct)
    curse(list, "foreach", pfclist.foreach)
    curse(list, "group_by", pfclist.group_by)
    curse(list, "is_empty", pfclist.is_empty)
    curse(list, "size", pfclist.size)
    curse(list, "find", pfclist.find)
    curse(list, "index_of", pfclist.index_of)
    curse(list, "fold_left", pfclist.fold_left)
    curse(list, "fold_right", pfclist.fold_right)
    curse(list, "forall", pfclist.forall)
    curse(list, "head", pfclist.head)
    curse(list, "tail", pfclist.tail)
    curse(list, "take", pfclist.take)
    curse(list, "length", pfclist.length)
    curse(list, "to_iterator", pfclist.to_iterator)

    # Parallel operations
    curse(list, "par_map", pfclist.par_map)
    curse(list, "par_filter", pfclist.par_filter)
    curse(list, "par_filter_not", pfclist.par_filter_not)
    curse(list, "par_flat_map", pfclist.par_flat_map)

    # Pure operations
    curse(list, "pure_map", pfclist.pure_map)
    curse(list, "pure_flat_map", pfclist.pure_flat_map)
    curse(list, "pure_filter", pfclist.pure_filter)
    curse(list, "pure_filter_not", pfclist.pure_filter_not)

    # Lazy operations
    curse(list, "lazy_map", pfclist.lazy_map)
    curse(list, "lazy_flat_map", pfclist.lazy_flat_map)
    curse(list, "lazy_filter", pfclist.lazy_filter)
    curse(list, "lazy_filter_not", pfclist.lazy_filter_not)
    curse(list, "lazy_flatten", pfclist.lazy_flatten)
    curse(list, "lazy_distinct", pfclist.lazy_distinct)
    curse(list, "lazy_take", pfclist.lazy_take)


def extend_set():
    """
    Extends the set and frozenset built-in type with methods.
    """
    curse(set, "map", pfcset.map)
    curse(set, "filter", pfcset.filter)
    curse(set, "filter_not", pfcset.filter_not)
    curse(set, "flat_map", pfcset.flat_map)
    curse(set, "contains", pfcset.contains)
    curse(set, "foreach", pfcset.foreach)
    curse(set, "group_by", pfcset.group_by)
    curse(set, "is_empty", pfcset.is_empty)
    curse(set, "size", pfcset.size)
    curse(set, "find", pfcset.find)
    curse(set, "fold_left", pfcset.fold_left)
    curse(set, "fold_right", pfcset.fold_right)
    curse(set, "forall", pfcset.forall)
    curse(set, "length", pfcset.length)
    curse(set, "to_iterator", pfcset.to_iterator)

    curse(frozenset, "map", pfcset.map)
    curse(frozenset, "filter", pfcset.filter)
    curse(frozenset, "filter_not", pfcset.filter_not)
    curse(frozenset, "flat_map", pfcset.flat_map)
    curse(frozenset, "contains", pfcset.contains)
    curse(frozenset, "foreach", pfcset.foreach)
    curse(frozenset, "group_by", pfcset.group_by)
    curse(frozenset, "is_empty", pfcset.is_empty)
    curse(frozenset, "size", pfcset.size)
    curse(frozenset, "find", pfcset.find)
    curse(frozenset, "fold_left", pfcset.fold_left)
    curse(frozenset, "fold_right", pfcset.fold_right)
    curse(frozenset, "forall", pfcset.forall)
    curse(frozenset, "length", pfcset.length)
    curse(frozenset, "to_iterator", pfcset.to_iterator)

    # Parallel operations
    curse(set, "par_map", pfcset.par_map)
    curse(set, "par_filter", pfcset.par_filter)
    curse(set, "par_filter_not", pfcset.par_filter_not)
    curse(set, "par_flat_map", pfcset.par_flat_map)

    curse(frozenset, "par_map", pfcset.par_map)
    curse(frozenset, "par_filter", pfcset.par_filter)
    curse(frozenset, "par_filter_not", pfcset.par_filter_not)
    curse(frozenset, "par_flat_map", pfcset.par_flat_map)

    # Pure operations
    curse(set, "pure_map", pfcset.pure_map)
    curse(set, "pure_flat_map", pfcset.pure_flat_map)
    curse(set, "pure_filter", pfcset.pure_filter)
    curse(set, "pure_filter_not", pfcset.pure_filter_not)

    curse(frozenset, "pure_map", pfcset.pure_map)
    curse(frozenset, "pure_flat_map", pfcset.pure_flat_map)
    curse(frozenset, "pure_filter", pfcset.pure_filter)
    curse(frozenset, "pure_filter_not", pfcset.pure_filter_not)

    # Lazy operations
    curse(set, "lazy_map", pfcset.lazy_map)
    curse(set, "lazy_flat_map", pfcset.lazy_flat_map)
    curse(set, "lazy_filter", pfcset.lazy_filter)
    curse(set, "lazy_filter_not", pfcset.lazy_filter_not)

    curse(frozenset, "lazy_map", pfcset.lazy_map)
    curse(frozenset, "lazy_flat_map", pfcset.lazy_flat_map)
    curse(frozenset, "lazy_filter", pfcset.lazy_filter)
    curse(frozenset, "lazy_filter_not", pfcset.lazy_filter_not)


if EXTEND_BUILTINS:
    extend_dict()
    extend_list()
    extend_set()
