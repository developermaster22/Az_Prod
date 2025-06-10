from django.contrib import admin
from .models import Pedido, Seguimiento

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'cliente', 'estado', 'fecha_creacion')
    search_fields = ('codigo', 'cliente')
    list_filter = ('estado',)

@admin.register(Seguimiento)
class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'rol', 'usuario', 'estado', 'fecha')
    search_fields = ('usuario', 'pedido__codigo')
    list_filter = ('rol', 'estado')
