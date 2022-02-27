#!/usr/bin/env -S bash -e

PYTHONPATH=. poetry run pytest --cov simulation --cov-report html --cov-report term
