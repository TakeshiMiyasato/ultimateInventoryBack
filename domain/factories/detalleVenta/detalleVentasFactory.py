from domain.model.detalleVenta import DetalleVenta


class DetalleVentasFactory:
    def composeArrDetalleVentas(self, request):
        array = []
        for x in request:
            array.append(DetalleVenta(x))
        return array