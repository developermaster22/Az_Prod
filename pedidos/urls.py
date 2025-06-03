from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    CustomLoginView,
    lista_pedidos,
    detalle_pedido,
    crear_pedido,
    agregar_seguimiento,
    dashboard,
    procesar_pedido,
    vista_administradores,
    vista_designers,
    vista_enteladores,
    vista_impresores,
    vista_embolsadores,
)

urlpatterns = [
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("", dashboard, name="dashboard"),
    path("pedidos/", lista_pedidos, name="lista_pedidos"),
    path("pedidos/crear/", crear_pedido, name="crear_pedido"),
    path("pedidos/<str:codigo>/", detalle_pedido, name="detalle_pedido"),
    path(
        "pedidos/<str:codigo>/agregar_seguimiento/",
        agregar_seguimiento,
        name="agregar_seguimiento",
    ),
    path("pedidos/<str:codigo>/procesar/", procesar_pedido, name="procesar_pedido"),
    path("vista_administradores/", vista_administradores, name="vista_administradores"),
    path("vista_designers/", vista_designers, name="vista_designers"),
    path("vista_enteladores/", vista_enteladores, name="vista_enteladores"),
    path("vista_impresores/", vista_impresores, name="vista_impresores"),
    path("vista_embolsadores/", vista_embolsadores, name="vista_embolsadores"),
]
