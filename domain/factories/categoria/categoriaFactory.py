from domain.model.categoria import Categoria


class CategoriaFactory:
    def createCategoria(self, request):
        return Categoria(request)
