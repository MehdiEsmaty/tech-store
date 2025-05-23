#!/bin/bash
python -c "from app import db; db.create_all()"
python seed_data.py
python app.py 