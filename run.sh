#!/usr/bin/env bash

MASSA_ROOT="$(cd "$(dirname "${0}")"; echo $(pwd))"

exec "${MASSA_ROOT}/.virtualenv/bin/gunicorn" \
    --name massa \
    --bind unix:/tmp/gunicorn.massa.sock \
    --workers 2 \
    "massa:create_app()"
