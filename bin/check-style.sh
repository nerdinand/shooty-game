#!/usr/bin/env -S bash -xe

# TODO: remove || true once everything is documented
poetry run pydocstyle --count || true
poetry run pylint **/*.py
