# Introduction

[pyfuncol](https://github.com/didactic-meme/pyfuncol) is a Python functional collections library. It _extends_ collections built-in types with useful methods to write functional Python code. It uses [Forbidden Fruit](https://github.com/clarete/forbiddenfruit) under the hood.

pyfuncol provides:

- Standard "eager" methods, such as `map`, `flat_map`, `group_by`, etc.
- Parallel methods, such as `par_map`, `par_flat_map`, etc.
- Pure methods that leverage memoization to improve performance, such as `pure_map`, `pure_flat_map`, etc.
- Lazy methods that return iterators and never materialize results, such as `lazy_map`, `lazy_flat_map`, etc.

pyfuncol can also be [used without forbiddenfruit](usage-without-forbiddenfruit).
