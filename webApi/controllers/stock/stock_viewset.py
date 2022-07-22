from rest_framework import viewsets
from rest_framework.decorators import action

from webApi.controllers.mediator import Mediator
from infraestructure.models import Stock
from infraestructure.persistance.services.stock.stockService import StockSerializer


class StockViewSet(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

    @action(detail=False, methods=['POST'])
    def actualizarStock(self, request):
        return Mediator.WriteDb(self, request, action='actualizarStock')

    @action(detail=False, methods=['POST'])
    def getStockByProducto(self, request):
        return Mediator.ReadDb(self, request, action='getStockByProducto')

    @action(detail=False, methods=['POST'])
    def getHistorialByProducto(self, request):
        return Mediator.ReadDb(self, request, action='getHistorialByProducto')