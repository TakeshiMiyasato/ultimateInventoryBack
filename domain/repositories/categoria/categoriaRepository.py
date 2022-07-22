from domain.model.categoria import Categoria
from infraestructure.persistance.services.categoria.categoriaService import CategoriaService
from shareKernel.core.EventHandler import EventHandler

event_handler = EventHandler()


class CategoriaRepository:

    def createCategoria(self, request):
        return CategoriaService.createCategoria(self, request, event_handler)

    def updateCategoria(self, request, obj_categoria):
        return CategoriaService.updateCategoria(self, request, obj_categoria, event_handler)

    def getAllCategorias(self, request):
        return CategoriaService.getAllCategorias(self, request)

    def getCategoriaById(self, request):
        return CategoriaService.getCategoriasById(self, request)
