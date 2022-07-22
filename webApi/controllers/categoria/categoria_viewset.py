from rest_framework import viewsets
from rest_framework.decorators import action

from webApi.controllers.mediator import Mediator
from infraestructure.models import Categoria
from infraestructure.persistance.services.categoria.categoriaService import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

    @action(detail=False, methods=['GET'])
    def getAllCategorias(self, request):
        return Mediator.ReadDb(self, request, action='getAllCategorias')

    @action(detail=False, methods=['POST'])
    def getCategoriaById(self, request):
        return Mediator.ReadDb(self, request, action='getCategoriaById')

    @action(detail=False, methods=['POST'])
    def createCategoria(self, request):
        return Mediator.WriteDb(self, request, action='createCategoria')

    @action(detail=False, methods=['PATCH'])
    def updateCategoria(self, request):
        return Mediator.WriteDb(self, request, action='updateCategoria')