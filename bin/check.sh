#!/usr/bin/env bash -e

poetry run reorder-python-imports **/*.py
poetry run black .
poetry run pylint **/*.py
poetry run pyre --strict check
PYTHONPATH=. poetry run pytest
