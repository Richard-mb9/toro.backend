#!/bin/sh

if [ $# -ne 0 ]; then
    exec "$@"
else
    exec chmod +x ./update_database.sh &
    exec ./update_database.sh &
    exec gunicorn -b :8080 -k uvicorn.workers.UvicornWorker app:app
fi