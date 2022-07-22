from domain.factories.detalleVenta.detalleVentasFactory import DetalleVentasFactory
from domain.model.venta import Venta
from domain.repositories.venta.ventaRepository import VentaRepository


class VentaFactory:
    def createVenta(self, request):
        return Venta(request)