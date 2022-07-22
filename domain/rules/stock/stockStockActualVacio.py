from infraestructure.models import Stock


class StockStockActualVacio:
    def applyRule(self, producto, emitido, agregado):
        stockActual = Stock.objects.filter(producto_id=producto).last().stockActual

        if stockActual == 0 and emitido > 0:
            raise Exception('No puedes emitir nada, el stock actual del producto esta vacio')
        elif emitido == 0 and agregado == 0:
            raise Exception('No se puede agregar una transaccion si no hay agregado o emitido')
        else:
            stockActual += agregado
            stockActual -= emitido
            return stockActual
