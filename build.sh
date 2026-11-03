#!/usr/bin/env bash
# Script de build do Render: instala dependencias, prepara estaticos e banco.
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate --no-input
python manage.py shell -c "exec(open('populate_db.py', encoding='utf-8').read())"
# Cria o superusuario a partir das variaveis DJANGO_SUPERUSER_USERNAME/EMAIL/PASSWORD
python manage.py createsuperuser --no-input || true
