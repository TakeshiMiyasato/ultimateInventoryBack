from domain.factories.categoria.categoriaFactory import CategoriaFactory


class UpdateCategoriaCommand:
    def updateCategoriaCommand(self, request):
        return CategoriaFactory.createCategoria(self, request)
