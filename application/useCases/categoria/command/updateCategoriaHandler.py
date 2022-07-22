from pymitter import EventEmitter

from application.useCases.categoria.command.updateCategoriaCommand import UpdateCategoriaCommand
from domain.factories.categoria.categoriaFactory import CategoriaFactory
from domain.repositories.categoria.categoriaRepository import CategoriaRepository


class UpdateCategoriaHandler:

    def updateCategoria(self, request):
        obj_categoria = UpdateCategoriaCommand.updateCategoriaCommand(self, request)
        return CategoriaRepository.updateCategoria(self, request, obj_categoria)
