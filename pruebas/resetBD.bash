#!/bin/bash
# Script de prueba

rm apl.db 
rm -r migrations/
rm -r __pycache__/
python base.py db init
python base.py db migrate
python base.py db upgrade


