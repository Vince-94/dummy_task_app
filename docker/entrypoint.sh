#!/bin/bash
set -e


if [[ -n "$CI" ]]; then
    exec /bin/bash
else
    exec "$@"
fi
