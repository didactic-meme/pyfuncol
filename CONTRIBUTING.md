# Contributing

## Setup

Fork the repo, then install all development requirements with:

```shell
pip install -r development.txt
```

When your changes are ready, submit a pull request!

## Style

For formatting and code style, we use [black](https://github.com/psf/black). Docstrings should follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings).

## Tests

To run the tests, execute `pytest` at the root of the project.

To run the tests with coverage enabled, execute:

```shell
pytest --cov-config=.coveragerc --cov=pyfuncol --cov-report=xml
```

## Docs

The docs are hosted on [Read the Docs](https://pyfuncol.readthedocs.io/en/latest/). Source files are in `docs/source/`.

To build them locally, run in `docs/`:

```shell
make html
```

The HTML files will be stored in `docs/build/`.

## Project structure

```
┌── docs - Contains the docs source code
├── pyfuncol - Contains all the library source code
    ├── tests - Contains tests for all the modules
    ├── __init__.py - Contains the function calls that extend built-in types
    ├── dict.py - Contains extension functions for dictionaries
    ├── list.py - Contains extension functions for lists
    └── ...
└── ...
```

## Release

To publish a new release on [PyPI](https://pypi.org/project/pyfuncol/):

1. Update the version in `setup.py`
2. Update the version (`release` field) in `docs/source/conf.py`
3. Push the version bump
4. Create a new release on [GitHub](https://github.com/didactic-meme/pyfuncol/releases). The newly created tag and the release title should match the version in `setup.py` and `docs/source/conf.py` with 'v' prepended. An example: for version `1.1.1`, the tag and release title should be `v1.1.1`.

The GitHub release creation will trigger the deploy workflow that builds and uploads the project to PyPI.

## Code of Conduct

Our Code of Conduct is [here](https://github.com/didactic-meme/pyfuncol/blob/main/CODE_OF_CONDUCT.md). By contributing to pyfuncol, you implicitly accept it.
