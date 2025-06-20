#!/usr/bin/env bash
set -euo pipefail

# 1. Ir al directorio correcto (¡crucial!)
cd /opt/render/project/src

# 2. Instalar dependencias
poetry install --no-interaction

# 3. Migraciones y estáticos
python manage.py migrate --noinput
python manage.py collectstatic --noinput