python3 -m pip install -U pip
python3 -m pip install -r requirements.txt
python3 main.py

#!/bin/bash
uvicorn main:app --host=0.0.0.0 --port=$PORT
