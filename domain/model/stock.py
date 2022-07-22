from domain.rules.stock.stockAgregadoControl import StockAgregadoControl
from domain.rules.stock.stockEmitidoControl import StockEmitidoControl
from domain.rules.stock.stockStockActualVacio import StockStockActualVacio
from domain.valueObjects.stock.stockAgregadoVO import StockAgregadoVO
from domain.valueObjects.stock.stockEmitidoVO import StockEmitidoVO
from domain.valueObjects.stock.stockStockActualVO import StockStockActualVO


class Stock:
    def __init__(self, request):
        self.producto = request.data['producto']
        self.agregado = StockAgregadoVO.StockAgregado(self, request.data['agregado'], request.data['emitido'])
        self.emitido = StockEmitidoVO.StockEmitido(self, request.data['agregado'], request.data['emitido'])
        self.stockActual = StockStockActualVO.StockStockActual(self, self.producto, self.emitido, self.agregado)
        print("Stock actual = " + str(self.stockActual))