#!/bin/bash
echo "Template API Mode is: $ENV"

# Start Application
if [[ "$APPLICATION_NAME" == "worker" ]];then
    echo "Starting Redis Worker"
    python3 -u /opt/src/worker.py
    exit 1
fi
GUNI_CONFIG="/opt/src/gunicorn_${ENV}.conf.py"
LOG_CONFIG="/opt/src/logging.conf"

gunicorn --log-config "$LOG_CONFIG" \
         --config "$GUNI_CONFIG" \
         wsgi:app
