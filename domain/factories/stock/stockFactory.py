from domain.model.stock import Stock
from domain.repositories.stock.stockRepository import StockRepository


class StockFactory:
    def createStock(self, request):
        return Stock(request)
