#!/usr/bin/env bash

set -o errexit
set -o nounset

MASSA_ROOT="$(cd "$(dirname "${0}")"; echo $(pwd))"
ENV_FILE="${MASSA_ROOT}/.env"

if [ -f "${ENV_FILE}" ]; then
    source "${ENV_FILE}"
fi

exec "${MASSA_ROOT}/.virtualenv/bin/gunicorn" \
    --name massa \
    --bind unix:/tmp/gunicorn.massa.sock \
    --workers 2 \
    "massa:create_app()"
