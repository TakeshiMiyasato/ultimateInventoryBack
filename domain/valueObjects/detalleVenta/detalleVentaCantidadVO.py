from domain.rules.detalleVenta.detalleVentaCantidadStockLimite import DetalleVentaCantidadStockLimite


class DetalleVentaCantidadVO:
    def DetalleVentaCantidad(self, cantidad, producto):
        return DetalleVentaCantidadStockLimite.applyRule(self, cantidad, producto)