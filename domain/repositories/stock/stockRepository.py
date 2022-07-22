from infraestructure.persistance.services.stock.stockService import StockService
from shareKernel.core.EventHandler import EventHandler

event_handler = EventHandler()

class StockRepository:
    def actualizarStock(self, request):
        return StockService.actualizarStock(self, request, event_handler)

    def getStockByProducto(self, request):
        return StockService.getStockByProducto(self, request)

    def getHistorialByProducto(self, request):
        return StockService.getHistorialByProducto(self, request)