from rest_framework import serializers
from rest_framework.response import Response

from infraestructure.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'producto', 'agregado', 'emitido', 'stockActual', 'fecha', 'producto_nombre')


class StockService:

    def actualizarStock(self, obj_stock, event_handler):
        stock = Stock()
        stock.producto_id = obj_stock.producto
        stock.agregado = obj_stock.agregado
        stock.emitido = obj_stock.emitido
        stock.stockActual = obj_stock.stockActual
        print(obj_stock.stockActual)
        stock.save()
        serializer = StockSerializer(stock, many=False)
        return Response(serializer.data)

    def crearRegistroStock(self, obj_stock):
        obj_stock.save()
        serializer = StockSerializer(obj_stock, many=False)
        return Response(serializer.data)

    def getStockByProducto(self, request):
        stock = Stock.objects.filter(producto_id=request.data['producto']).last()
        serializer = StockSerializer(stock, many=False)
        return Response(serializer.data)

    def getHistorialByProducto(self, request):
        stock = Stock.objects.filter(producto_id=request.data['producto']).order_by('-fecha')
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)
