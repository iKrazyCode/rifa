from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ...


class Comprador(models.Model):
    """
    Comprador das rifas
    """
    nome = models.CharField(verbose_name='nome do comprador', max_length=300)
    cpf = models.CharField(verbose_name='cpf do comprador', max_length=11)
    telefone = models.CharField(verbose_name='Número de celular', max_length=20)

    def __str__(self):
        return self.nome

