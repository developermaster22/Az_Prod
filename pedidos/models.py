from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import uuid
from accounts.models import CustomUser




ESTADOS = [
    ("pendiente", "Pendiente"),
    ("en_proceso", "En proceso"),
    ("completado", "Completado"),
    ("pausado", "Pausado"),
]


class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(
        max_length=20, unique=True, blank=True
    )  # Se genera en save()
    cliente = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="pedidos/", blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")

    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pedidos_creados",
    )
    actualizado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pedidos_actualizados",
    )
    actualizado_en = models.DateTimeField(null=True, blank=True)

    observacion = models.TextField(blank=True, null=True)  # Para motivo de devolución

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = f"P{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.codigo


class Seguimiento(models.Model):
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, related_name="seguimientos"
    )
    rol = models.CharField(max_length=20, choices=CustomUser.ROLE_CHOICES)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    estado = models.CharField(max_length=20, choices=ESTADOS)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pedido.codigo} - {self.get_rol_display()} - {self.estado}"