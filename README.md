# Purpose

The purpose of this repo is to host the code implementation and writeup for 
a nontrivial permutation on the natural numbers. The precise meaning of 
"nontrivial" is not yet formalized, but a key conjecture is that there may 
be no upper bound to the length of cycles.

Please refer to [WRITEUP.md](WRITEUP.md) for more details.

# Install

Please execute the following from within your preferred development environment (venv, miniconda, etc..):

```
pip install naturalperm
```

This will install dependencies and bind the CLI.

# Developers

Development is managed through `make` and `poetry`. Please ensure that your
development environment supports `make` v4.0 or later. Executing `make help`
will print the full set of available options. Here are top use cases:

```
## install poetry if it is not installed already
## execute `poetry install` to set up poetry virtual environment
make install

## execute unit tests only
make test

## print full set of make options
make help
```

If you have not used poetry before, the key thing to know is, to
execute a command within the virtual environment, you simply do
```
$ poetry run COMMAND
```

