from domain.rules.stock.stockEmitidoControl import StockEmitidoControl


class StockEmitidoVO:
    def StockEmitido(self, agregado, emitido):
        return StockEmitidoControl.applyRule(self, agregado, emitido)