#!/usr/bin/env bash
set -euo pipefail

# Configurar Poetry
export PIP_USER=no
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true

# Instalar dependencias
poetry install --no-interaction --no-ansi

# Activar entorno y asegurar Gunicorn
source .venv/bin/activate
pip install gunicorn

# Migraciones y archivos estáticos
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear