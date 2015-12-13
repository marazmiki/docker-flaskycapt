#!/bin/bash

set -e

PORT=8765
DISPLAY=99

mkdir -p ~/.xpra;
xpra start :${DISPLAY}

gunicorn app:app            \
    --bind=0.0.0.0:${PORT}  \
    --workers 5             \
    --log-level=info        \
    --log-file=-            \
    --access-logfile=-      \
    "$@"
