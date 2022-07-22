from infraestructure.persistance.services.venta.ventaService import VentaService
from shareKernel.core.EventHandler import EventHandler

event_handler = EventHandler()

class VentaRepository:
    def createVenta(self, obj_venta, arr_detalleVentas):
        return VentaService.createVenta(self, obj_venta, arr_detalleVentas, event_handler)

    def getVentasByUser(self, request):
        return VentaService.getVentasByUser(self, request)

    def getVentaById(self, request):
        return VentaService.getVentaById(self, request)

    def getVentasPendientes(self, request):
        return VentaService.getVentasPendientes(self, request)

    def getVentasAnuladasRechazadas(self, request):
        return VentaService.getVentasAnuladasRechazadas(self, request)

    def getVentasEntregadas(self, request):
        return VentaService.getVentasEntregadas(self, request)

    def creadoPagado(self, request):
        return VentaService.creadoPagado(self, request)

    def pagadoAceptado(self, request):
        return VentaService.pagadoAceptado(self, request)

    def pagadoRechazado(self, request):
        return VentaService.pagadoRechazado(self, request)

    def aceptadoEntragado(self, request):
        return VentaService.aceptadoEntregado(self, request)

    def anular(self, request):
        return VentaService.anular(self, request, event_handler)
