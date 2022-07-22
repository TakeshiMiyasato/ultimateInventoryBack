from rest_framework import viewsets
from rest_framework.decorators import action

from webApi.controllers.mediator import Mediator
from infraestructure.models import DetalleVenta
from infraestructure.persistance.services.venta.ventaService import DetalleVentaSerializer


class DetalleVentaViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleVentaSerializer
    queryset = DetalleVenta.objects.all()

    @action(detail=False, methods=['POST'])
    def getDetalleVentasByVenta(self, request):
        return Mediator.ReadDb(self, request, action='getDetalleVentasByVenta')
