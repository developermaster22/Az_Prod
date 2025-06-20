#!/usr/bin/env bash
set -euo pipefail

# Instalar dependencias
poetry install --no-interaction

# Aplicar migraciones
python manage.py migrate --noinput

# Crear superusuario (opcional)
if [ -z "$(python manage.py shell -c 'from accounts.models import CustomUser; print(CustomUser.objects.exists())')" ]; then
    echo "from accounts.models import CustomUser; CustomUser.objects.create_superuser('admin_temp', 'admin@example.com', 'TempPass123!')" | python manage.py shell
fi

# Colectar archivos estáticos
python manage.py collectstatic --noinput