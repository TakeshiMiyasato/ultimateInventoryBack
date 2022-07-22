from domain.rules.stock.stockStockActualVacio import StockStockActualVacio


class StockStockActualVO:
    def StockStockActual(self, producto, emitido, agregado):
        return StockStockActualVacio.applyRule(self, producto, emitido, agregado)