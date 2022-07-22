from domain.factories.detalleVenta.detalleVentasFactory import DetalleVentasFactory


class CrearArrayDetalleVentasCommand:
    def crearArrayDetalleVentas(self, request):
        return DetalleVentasFactory.composeArrDetalleVentas(self, request.data['detallesVentas'])