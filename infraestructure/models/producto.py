from builtins import property

from django.db import models

from infraestructure.models import Categoria


class Producto(models.Model):
    precio = models.IntegerField(null=False, default=0)
    nombre = models.CharField(null=False, max_length=200)
    descripcion = models.CharField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='producto_categoria')

    @property
    def categoria_nombre(self):
        return self.categoria.nombre


