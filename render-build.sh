#!/usr/bin/env bash
set -euo pipefail

# Debug
echo "=== Estructura actual ==="
ls -la

# Instalar dependencias (ya estás en /opt/render/project/src)
poetry install --no-interaction

# Migraciones (el manage.py está en la raíz)
python manage.py migrate --noinput

# Archivos estáticos
python manage.py collectstatic --noinput