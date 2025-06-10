
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('diseñador', 'Diseñador'),
        ('impresor', 'Impresor'),
        ('entelador', 'Entelador'),
        ('embolsador', 'Embolsador'),
        ('administrador', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default='diseñador')
