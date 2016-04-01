#!/bin/bash
# Script de prueba

python base.py db init
python base.py db migrate
python base.py db upgrade


