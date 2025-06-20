#!/usr/bin/env bash
set -euo pipefail

# Debug: Ver estructura de archivos
echo "=== Directorio actual: $(pwd) ==="
ls -la

# Entrar al directorio del proyecto
cd AZ_Prod

# Instalar dependencias
poetry install --no-interaction

# Aplicar migraciones
python manage.py migrate --noinput

# Colectar archivos estáticos
python manage.py collectstatic --noinput

echo "=== Build completado ==="