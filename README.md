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
  - [Contributing](#contributing)
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

{1, 2, 3, 4}.map(lambda x: x * 2).filter(lambda x: x > 4)
# {6, 8}

["abc", "def", "e"].group_by(lambda s: len(s))
# {3: ["abc", "def"], 1: ["e"]}

{"a": 1, "b": 2, "c": 3}.flat_map(lambda kv: {kv[0]: kv[1] ** 2})
# {"a": 1, "b": 4, "c": 9}
```

### API

For lists, please refer to the [docs](https://pyfuncol.readthedocs.io/en/latest/pyfuncol.html#module-pyfuncol.list).

For dictionaries, please refer to the [docs](https://pyfuncol.readthedocs.io/en/latest/pyfuncol.html#module-pyfuncol.dict).

For sets, please refer to the [docs](https://pyfuncol.readthedocs.io/en/latest/pyfuncol.html#module-pyfuncol.set).

For more details, please have a look at the [API reference](https://pyfuncol.readthedocs.io/en/latest/modules.html).

## Documentation

See <https://pyfuncol.readthedocs.io/>.

## Compatibility

Since it depends on [Forbidden Fruit](https://github.com/clarete/forbiddenfruit), it only works on CPython.

## Contributing

See the [contributing guide](https://github.com/Gondolav/pyfuncol/blob/main/CONTRIBUTING.md) for detailed instructions on how to get started with the project.

## License

pyfuncol is licensed under the [MIT license](https://github.com/Gondolav/pyfuncol/blob/main/LICENSE).
