#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]; then # mac os
    /usr/local/opt/postgres/bin/createuser -s postgres # setup db for first time use
    /usr/local/opt/postgres/bin/createdb gm-manager-db -U postgres # setup db for first time use
    pg_ctl -D /usr/local/var/postgres start

elif [[ "$OSTYPE" == "msys" ]]; then # windows git bash
    echo "windows witg git bash"
    # cmd "D:\Program Files (x64)\PostgreSQL\scripts\runpsql.bat"
fi
