#!/usr/bin/env bash
set -euo pipefail

# Debug: Ver estructura y variables
echo "=== Estructura inicial ==="
ls -la
echo "=== Variables de entorno ==="
printenv | grep -E 'DATABASE_URL|STATIC_|SECRET_KEY'

# 1. Crear directorio para staticfiles
mkdir -p staticfiles

# 2. Instalar dependencias
echo "=== Instalando dependencias ==="
poetry install --no-interaction

# 3. Aplicar migraciones
echo "=== Aplicando migraciones ==="
python manage.py migrate --noinput

# 4. Crear superusuario si no existe (VERSIÓN CORREGIDA)
echo "=== Verificando superusuario ==="
if ! python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='admin').exists())" | grep -q "True"; then
    echo "=== Creando superusuario ==="
    python manage.py createsuperuser \
        --username admin \
        --email admin@azprod.com \
        --noinput || \
    python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@azprod.com', 'AzProdAdmin123!')
print('Superusuario creado exitosamente')
"
else
    echo "El superusuario 'admin' ya existe"
fi

# 5. Colectar archivos estáticos
echo "=== Colectando archivos estáticos ==="
python manage.py collectstatic --noinput --clear

# Debug final
echo "=== Estructura final ==="
ls -la
echo "=== Proceso completado ==="