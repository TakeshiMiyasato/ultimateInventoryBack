from domain.rules.stock.stockAgregadoControl import StockAgregadoControl


class StockAgregadoVO:
    def StockAgregado(self, agregado, emitido):
        return StockAgregadoControl.applyRule(self, agregado, emitido)