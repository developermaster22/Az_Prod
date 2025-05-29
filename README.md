# Az_Prod

Sistema de gestión de pedidos para AZ Paneles.

---

## Descripción

Az_Prod es una aplicación web desarrollada en Django para gestionar el flujo de trabajo de pedidos en AZ Paneles.  
Permite que diferentes roles (Diseñador, Impresor, Entelador, Embolsador y Administrador) colaboren en el procesamiento de pedidos con control de estados, devoluciones y observaciones.

---

## Características principales

- Registro y gestión de pedidos con generación automática de código.
- Subida de diseños por parte del Diseñador.
- Control de estados secuenciales por rol: Diseñador → Impresor → Entelador → Embolsador.
- Sistema de devolución con motivo y observaciones para corregir errores.
- Dashboard personalizado según el rol del usuario.
- Registro de historial y seguimiento de cada pedido.

---

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone git@github.com:developermaster22/Az_Prod.git
   cd Az_Prod

2. Crear y activar un entorno virtual:

#bash

python3 -m venv env
source env/bin/activate  # Linux / macOS
env\Scripts\activate     # Windows

3. Instalar dependencias:

#bash

pip install -r requirements.txt

4. Configurar base de datos y variables de entorno (editar settings.py o usar .env).

5. Ejecutar migraciones:

#bash

python manage.py migrate

6. Crear usuario administrador:

bash
python manage.py createsuperuser

7. Ejecutar servidor local:

bash

python manage.py runserver

Uso
Acceder al sistema en http://localhost:8000.

Iniciar sesión con un usuario con rol asignado.

Usar el dashboard para ver y procesar pedidos según el rol.

Crear pedidos (rol Diseñador y Administrador).

Procesar pedidos, aprobar o devolver con observación.

Visualizar historial y detalles de pedidos.

Roles de usuario
Administrador: Acceso completo, puede crear pedidos y administrar usuarios.

Diseñador: Subir diseños y crear pedidos.

Impresor: Procesar pedidos después de diseño, puede devolver pedidos.

Entelador: Procesar pedidos después de impresión, puede devolver pedidos.

Embolsador: Procesar pedidos finales, puede devolver pedidos.

Contribuciones
Si quieres contribuir, por favor abre un issue o envía un pull request.

Licencia
Indicar la licencia que usarás (MIT, GPL, etc).

Contacto
César Linares — [cesarlinares1522@gmail.com]

Este README fue creado para documentar y guiar el desarrollo del proyecto Az_Prod.
