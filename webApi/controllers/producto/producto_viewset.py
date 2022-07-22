from rest_framework import viewsets
from rest_framework.decorators import action

from webApi.controllers.mediator import Mediator
from infraestructure.models import Producto
from infraestructure.persistance.services.producto.productoService import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    @action(detail=False, methods=['GET'])
    def getAllProductos(self, request):
        return Mediator.ReadDb(self, request, action='getAllProductos')

    @action(detail=False, methods=['POST'])
    def getProductoById(self, request):
        return Mediator.ReadDb(self, request, action='getProductoById')

    @action(detail=False, methods=['POST'])
    def getProductosByCategoria(self, request):
        return Mediator.ReadDb(self, request, action='getProductosByCategoria')

    @action(detail=False, methods=['POST'])
    def createProducto(self, request):
        return Mediator.WriteDb(self, request, action='createProducto')

    @action(detail=False, methods=['PATCH'])
    def updateProducto(self, request):
        return Mediator.WriteDb(self, request, action='updateProducto')