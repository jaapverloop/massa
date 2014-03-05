#!/usr/bin/env bash

MASSA_ROOT="$(cd "$(dirname "${0}")"; echo $(pwd))"
ENV_FILE="${MASSA_ROOT}/.env"

if [ ! -f "${ENV_FILE}" ]; then
    echo "The root directory does not contain the required `.env` file."
    echo "Copy the example file and make the necessary changes."
    exit 1
fi

source "${ENV_FILE}"

exec "${MASSA_ROOT}/.virtualenv/bin/gunicorn" \
    --name massa \
    --bind unix:/tmp/gunicorn.massa.sock \
    --workers 2 \
    "massa:create_app()"
