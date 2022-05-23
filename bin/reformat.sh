#!/usr/bin/env -S bash -xe

poetry run reorder-python-imports **/*.py
poetry run black .
