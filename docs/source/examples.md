# Examples

To use the methods, you just need to import pyfuncol. Some examples:

```python
import pyfuncol

[1, 2, 3, 4].map(lambda x: x * 2).filter(lambda x: x > 4)
# [6, 8]

[1, 2, 3, 4].fold_left(0, lambda acc, n: acc + n)
# 10

{1, 2, 3, 4}.map(lambda x: x * 2).filter_not(lambda x: x <= 4)
# {6, 8}

["abc", "def", "e"].group_by(lambda s: len(s))
# {3: ["abc", "def"], 1: ["e"]}

{"a": 1, "b": 2, "c": 3}.flat_map(lambda kv: {kv[0]: kv[1] ** 2})
# {"a": 1, "b": 4, "c": 9}
```

pyfuncol also provides parallel operations (for now `par_map`, `par_flat_map`, `par_filter` and `par_filter_not`):

```python
[1, 2, 3, 4].par_map(lambda x: x * 2).par_filter(lambda x: x > 4)
# [6, 8]

{1, 2, 3, 4}.par_map(lambda x: x * 2).par_filter_not(lambda x: x <= 4)
# {6, 8}

{"a": 1, "b": 2, "c": 3}.par_flat_map(lambda kv: {kv[0]: kv[1] ** 2})
# {"a": 1, "b": 4, "c": 9}
```

pyfuncol provides operations leveraging memoization to improve performance (for now `pure_map` and `pure_flat_map`). BEWARE: these versions work only
for **pure** functions (i.e., all calls to the same args return the same value)

```python
[1, 2, 3, 4].pure_map(lambda x: x * 2).filter(lambda x: x > 4)
# [6, 8]

{1, 2, 3, 4}.pure_map(lambda x: x * 2).filter_not(lambda x: x <= 4)
# {6, 8}

{"a": 1, "b": 2, "c": 3}.pure_flat_map(lambda kv: {kv[0]: kv[1] ** 2})
# {"a": 1, "b": 4, "c": 9}
```