#!/usr/bin/env -S bash -e

# TODO: remove || true once everything is documented
poetry run pydocstyle --count **/*.py || true
poetry run pylint **/*.py
