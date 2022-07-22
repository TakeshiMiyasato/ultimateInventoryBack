from domain.valueObjects.detalleVenta.detalleVentaCantidadVO import DetalleVentaCantidadVO
from infraestructure.models import Producto


class DetalleVenta:
    def __init__(self, request):
        self.producto = request['producto']
        self.cantidad = DetalleVentaCantidadVO.DetalleVentaCantidad(self, request['cantidad'], request['producto'])
        self.precioVenta = Producto.objects.get(pk=request['producto']).precio * request['cantidad']