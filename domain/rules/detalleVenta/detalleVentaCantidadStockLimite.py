from infraestructure.models import Stock


class DetalleVentaCantidadStockLimite:
    def applyRule(self, cantidad, producto):
        stock = Stock.objects.filter(producto_id=producto).last().stockActual
        if cantidad > stock:
            raise Exception('La cantidad que estas agregando es mayor a la del stock del producto')
        else:
            return cantidad
