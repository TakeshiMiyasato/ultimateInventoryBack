from builtins import property

from django.db import models

from infraestructure.models import Venta, Producto


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='venta_detalle')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='producto_detalle')
    cantidad = models.IntegerField(default=0)
    precioVenta = models.IntegerField(default=0)

    @property
    def producto_nombre(self):
        return self.producto.nombre