from application.useCases.categoria.command.crearCategoriaCommand import CrearCategoriaCommand
from domain.repositories.categoria.categoriaRepository import CategoriaRepository


class CrearCategoriaHandler:
    def crearCategoria(self, request):
        obj_categoria = CrearCategoriaCommand.crearCategoriaCommand(self, request)
        return CategoriaRepository.createCategoria(self, obj_categoria)
