#!/usr/bin/env -S bash -e

./bin/reformat.sh
./bin/check-style.sh
./bin/check-types.sh
./bin/run-tests.sh
