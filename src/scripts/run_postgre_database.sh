#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]; then # mac os
    pg_ctl -D /usr/local/var/postgres start
    /usr/local/opt/postgres/bin/createuser -s postgres # setup db for first time use
    /usr/local/opt/postgres/bin/createdb gm-manager-db -U postgres # setup db for first time use

elif [[ "$OSTYPE" == "msys" ]]; then # windows git bash
    echo "windows witg git bash"
    # cmd "D:\Program Files (x64)\PostgreSQL\scripts\runpsql.bat"
fi
