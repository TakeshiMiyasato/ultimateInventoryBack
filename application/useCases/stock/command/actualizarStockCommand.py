from domain.factories.stock.stockFactory import StockFactory


class ActualizarStockCommand:
    def actualizarStock(self, request):
        return StockFactory.createStock(self, request)