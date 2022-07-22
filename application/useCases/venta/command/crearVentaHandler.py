from application.useCases.venta.command.crearArrayDetalleVentasCommand import CrearArrayDetalleVentasCommand
from application.useCases.venta.command.crearVentaCommand import CrearVentaCommand
from domain.factories.detalleVenta.detalleVentasFactory import DetalleVentasFactory
from domain.factories.venta.ventaFactory import VentaFactory
from domain.repositories.venta.ventaRepository import VentaRepository


class CrearVentaHandler:
    def crearVenta(self, request):
        obj_venta = VentaFactory.createVenta(self, request.data['venta'])
        arr_detallesVenta = DetalleVentasFactory.composeArrDetalleVentas(self, request.data['detallesVentas'])
        return CrearVentaCommand.crearVentaCommand(self, obj_venta, arr_detallesVenta)