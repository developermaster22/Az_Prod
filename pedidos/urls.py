from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    path('pedido/<str:codigo>/', views.detalle_pedido, name='detalle_pedido'),
    path('pedido/crear/', views.crear_pedido, name='crear_pedido'),
    path('pedido/<str:codigo>/procesar/', views.procesar_pedido, name='procesar_pedido'),
    path('pedido/<str:codigo>/agregar-seguimiento/', views.agregar_seguimiento, name='agregar_seguimiento'),

    # Vistas por roles (opcional, según tu código)
    path('vista/administradores/', views.vista_administradores, name='vista_administradores'),
    path('vista/disenadores/', views.vista_designers, name='vista_designers'),
    path('vista/enteladores/', views.vista_enteladores, name='vista_enteladores'),
    path('vista/impresores/', views.vista_impresores, name='vista_impresores'),
    path('vista/embolsadores/', views.vista_embolsadores, name='vista_embolsadores'),
]
