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

all:     ## make build && make test && make publish
> make build && make test && make publish

build:   ## Verify code can build
> poetry build

test:    ## Run unit tests
> poetry run pytest

publish: ## Release a package
> poetry publish

install: ## Install dependencies
> poetry install

