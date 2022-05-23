#!/usr/bin/env -S bash -xe

./bin/reformat.sh
./bin/check-style.sh
./bin/check-types.sh
./bin/run-unit-tests.sh
