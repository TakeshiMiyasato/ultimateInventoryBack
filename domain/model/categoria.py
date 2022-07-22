from domain.rules.categoria.categoriaNombreLimite import CategoriaNombreLimite
from domain.valueObjects.categoria.categoriaNombreVO import CategoriaNombreVO


class Categoria:

    def __init__(self, request):
        self.nombre = CategoriaNombreVO.CategoriaNombre(self, request.data['nombre'])
