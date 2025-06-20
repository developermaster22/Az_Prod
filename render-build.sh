#!/usr/bin/env bash
set -euo pipefail

# Debug: Ver estructura y variables
echo "=== Estructura inicial ==="
ls -la
echo "=== Variables de entorno ==="
printenv | grep -E 'DATABASE_URL|STATIC_'

# 1. Crear directorio para staticfiles
mkdir -p staticfiles

# 2. Instalar dependencias (incluyendo el paquete actual)
poetry install --no-interaction

# 3. Aplicar migraciones
python manage.py migrate --noinput

# 4. Colectar archivos estáticos (con clear)
python manage.py collectstatic --noinput --clear

# Debug final
echo "=== Estructura final ==="
ls -la