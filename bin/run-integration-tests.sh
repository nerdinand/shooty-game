#!/usr/bin/env -S bash -xe

PYTHONPATH=. poetry run pytest -v -m "integration" --cov simulation --cov-report html --cov-report term
