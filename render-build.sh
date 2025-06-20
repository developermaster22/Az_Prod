#!/usr/bin/env bash
set -euo pipefail

# 1. Instalar dependencias
poetry install --no-interaction
poetry add psycopg2-binary

# 2. Migraciones (con reintentos)
for i in {1..3}; do
    python manage.py migrate --noinput && break || sleep 5
done

# 3. Crear superusuario (si no existe)
python manage.py shell -c "
from accounts.models import CustomUser
if not CustomUser.objects.filter(username='admin').exists():
    CustomUser.objects.create_superuser('admin', 'admin@azprod.com', 'Admin123!')
"

# 4. Archivos estáticos
python manage.py collectstatic --noinput