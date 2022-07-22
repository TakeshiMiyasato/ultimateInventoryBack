from domain.factories.categoria.categoriaFactory import CategoriaFactory


class CrearCategoriaCommand:
    def crearCategoriaCommand(self, request):
        return CategoriaFactory.createCategoria(self, request)