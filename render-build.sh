#!/usr/bin/env bash
set -euo pipefail

# 1. Configura Poetry
echo "=== Configurando Poetry ==="
export PIP_USER=no
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true

# 2. Instalar dependencias
echo "=== Instalando dependencias ==="
poetry install --no-interaction --no-ansi

# 3. Activar el entorno virtual
echo "=== Activando entorno virtual ==="
source .venv/bin/activate

# 4. Instalar Gunicorn explícitamente
echo "=== Instalando Gunicorn ==="
poetry add gunicorn

# 5. Configuración Django
echo "=== Aplicando migraciones ==="
python manage.py migrate --noinput

echo "=== Colectando archivos estáticos ==="
python manage.py collectstatic --noinput --clear

echo "=== Verificación final ==="
python -c "import django; print(f'Django {django.__version__} instalado correctamente')"