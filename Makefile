# recommended preamble
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

default: help

.PHONY: help all build test publish install

help:    ## Show this help.
> @fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

all:     ## Execute build, test, and publish targets
> make build && make test && make publish

build:   ## Verify code can build
> poetry build

do:      ## Execute the package (to dump Markdown or other analysis)
> poetry run python -m naturalperm

test:    ## Run unit tests
> poetry run pytest

publish: ## Release a package
> poetry publish

clean:   ## Remove build products
> rm -fr dist

install: ## Install dependencies
> @poetry version > /dev/null || \
>     curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
> poetry install
