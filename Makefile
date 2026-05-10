install:
	uv sync

update:
	uv lock --upgrade
	uv sync

run:
	uv run hexlet-python-package

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gen_diff --cov-report xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install update test lint selfcheck check build