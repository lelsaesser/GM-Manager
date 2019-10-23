#!/bin/bash

export FLASK_APP="../GM-Manager-Flask/app.py"
source /c/Anaconda3/etc/profile.d/conda.sh
source /opt/anaconda3/etc/profile.d/conda.sh
conda init bash
conda activate GM-Manager-Flask
pip install -r "../GM-Manager-Flask/requirements.txt"
flask run -h 0.0.0.0 # runs on 127.0.0.1:5000