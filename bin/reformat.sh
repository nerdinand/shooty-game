#!/usr/bin/env -S bash -e

poetry run reorder-python-imports **/*.py
poetry run black .
