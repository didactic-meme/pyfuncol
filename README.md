# pyfuncol

![CI](https://github.com/Gondolav/pyfuncol/actions/workflows/python-app.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/pyfuncol?color=blue)
[![Documentation Status](https://readthedocs.org/projects/pyfuncol/badge/?version=latest)](https://pyfuncol.readthedocs.io/en/latest/?badge=latest)
[![GitHub license](https://img.shields.io/github/license/Gondolav/pyfuncol)](https://github.com/Gondolav/pyfuncol/blob/main/LICENSE)

- [pyfuncol](#pyfuncol)
  - [Installation](#installation)
  - [Usage](#usage)
    - [API](#api)
  - [Documentation](#documentation)
  - [Compatibility](#compatibility)
  - [License](#license)

A Python functional collections library. It _extends_ collections built-in types with useful methods to write functional Python code. It uses [Forbidden Fruit](https://github.com/clarete/forbiddenfruit) under the hood.

## Installation

`pip install pyfuncol`

## Usage

To use the methods, you just need to import pyfuncol. Some examples:

```python
import pyfuncol

[1, 2, 3, 4].map(lambda x: x * 2).filter(lambda x: x > 4)
# [6, 8]

["abc", "def", "e"].group_by(lambda s: len(s))
# {3: ["abc", "def"], 1: ["e"]}

{"a": 1, "b": 2, "c": 3}.flat_map(lambda kv: {kv[0]: kv[1] ** 2})
# {"a": 1, "b": 4, "c": 9}
```

### API

For lists: `map`, `filter`, `flat_map`, `flatten`, `contains`, `distinct`, `foreach`, `group_by`, `is_empty`, `size`, `find`, `index_of`.

For dictionaries: `map`, `filter`, `flat_map`, `contains`, `foreach`, `is_empty`, `size`, `to_list`.

For more details, look at the [API reference](https://pyfuncol.readthedocs.io/#modules).

## Documentation

See <https://pyfuncol.readthedocs.io/>.

## Compatibility

Since it depends on [Forbidden Fruit](https://github.com/clarete/forbiddenfruit), it only works on CPython.

## License

pyfuncol is licensed under the [MIT license](LICENSE).
