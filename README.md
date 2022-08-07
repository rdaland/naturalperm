# Purpose

The purpose of this repo is to host the code implementation and writeup for a nontrivial permutation on the natural numbers. The precise meaning of "nontrivial" is not yet formalized, but a key conjecture is that there may be no upper bound to the length of cycles.

Please refer to [WRITEUP.md](WRITEUP.md) for more details.

# Install

Please execute the following from within your preferred development environment (venv, miniconda, etc..):

```
pip install naturalperm
```

This will install dependencies and bind the CLI.

# Developers

Development is managed through `make` and `poetry`. Please ensure that your development environment supports standard `make`. Here are the most common use cases:

```
## install poetry and setup poetry virtual environment
make install

## execute unit tests only
make test

## PR checks: auto-formatting, code linting, unit tests
make check

## print full set of make options
make help
```
