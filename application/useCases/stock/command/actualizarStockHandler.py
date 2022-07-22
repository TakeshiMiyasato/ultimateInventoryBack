from application.useCases.stock.command.actualizarStockCommand import ActualizarStockCommand
from domain.repositories.stock.stockRepository import StockRepository


class ActualizarStockHandler:
    def actualizarStock(self, request):
        obj_stock = ActualizarStockCommand.actualizarStock(self, request)
        return StockRepository.actualizarStock(self, obj_stock)