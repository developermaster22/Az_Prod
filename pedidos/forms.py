from django import forms
from .models import Pedido, Seguimiento

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['codigo', 'cliente', 'descripcion', 'imagen']

class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        fields = ['rol', 'usuario', 'estado', 'comentario']
