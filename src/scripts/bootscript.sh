#!/bin/bash

source "./run_postgre_database.sh" &
source "./run_flask_backend.sh" &
source "./run_angular_frontend.sh" &

echo "application running."
