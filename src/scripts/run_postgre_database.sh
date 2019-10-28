#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]; then # mac os
    pg_ctl -D /usr/local/var/postgres start

elif [[ "$OSTYPE" == "msys" ]]; then # windows git bash
    echo "windows witg git bash"
    # cmd "D:\Program Files (x64)\PostgreSQL\scripts\runpsql.bat"
fi
