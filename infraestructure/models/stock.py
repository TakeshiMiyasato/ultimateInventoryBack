from builtins import property
from datetime import datetime

from django.db import models

from infraestructure.models import Producto


class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='producto_stock')
    agregado = models.IntegerField(default=0, blank=True)
    emitido = models.IntegerField(default=0, blank=True)
    stockActual = models.IntegerField(default=0, blank=True)
    fecha = models.DateTimeField(default=datetime.now, blank=True)

    @property
    def producto_nombre(self):
        return self.producto.nombre