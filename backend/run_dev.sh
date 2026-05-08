#!/bin/bash
pip install -r requirements.txt
playwright install
uvicorn main:app --reload --host 0.0.0.0 --port 8000
