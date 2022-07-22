from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from webApi.controllers.mediator import Mediator
from infraestructure.models import Venta, Stock, DetalleVenta
from infraestructure.persistance.services.venta.ventaService import VentaSerializer, DetalleVentaSerializer


class VentaViewSet(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()

    @action(detail=False, methods=['POST'])
    def createVenta(self, request):
        return Mediator.WriteDb(self, request, action='createVenta')

    @action(detail=False, methods=['POST'])
    def getVentasByUser(self, request, ):
        return Mediator.ReadDb(self, request, action='getVentasByUser')

    @action(detail=False, methods=['POST'])
    def getVentaById(self, request, ):
        return Mediator.ReadDb(self, request, action='getVentaById')

    @action(detail=False, methods=['GET'])
    def getVentasPendientes(self, request):
        return Mediator.ReadDb(self, request, action='getVentasPendientes')

    @action(detail=False, methods=['GET'])
    def getVentasAnuladasRechazadas(self, request):
        return Mediator.ReadDb(self, request, action='getVentasAnuladasRechazadas')

    @action(detail=False, methods=['GET'])
    def getVentasEntregadas(self, request):
        return Mediator.ReadDb(self, request, action='getVentasEntregadas')

    ###################################################

    @action(detail=False, methods=['post'])
    def creadoPagado(self, request, pk=None):
        return Mediator.WriteDb(self, request, action='creadoPagado')

    @action(detail=False, methods=['post'], url_path='pagadoAceptado', name='pagadoAceptado')
    def pagadoAceptado(self, request, pk=None):
        return Mediator.WriteDb(self, request, action='pagadoAceptado')

    @action(detail=False, methods=['post'], url_path='pagadoRechazado', name='pagadoRechazado')
    def pagadoRechazado(self, request, pk=None):
        return Mediator.WriteDb(self, request, action='pagadoRechazado')

    @action(detail=False, methods=['post'], url_path='aceptadoEntregado', name='aceptadoEntregado')
    def aceptadoEntregado(self, request, pk=None):
        return Mediator.WriteDb(self, request, action='aceptadoEntregado')

    @action(detail=False, methods=['post'], url_path='anular', name='anular')
    def anular(self, request, pk=None):
        return Mediator.WriteDb(self, request, action='anular')
