#!/bin/bash
# Windows version

export FLASK_APP="../GM-Manager-Flask/app.py"
source /c/Anaconda3/etc/profile.d/conda.sh
conda activate GM-Manager-Flask
flask run -h 0.0.0.0 # runs on 127.0.0.1:5000