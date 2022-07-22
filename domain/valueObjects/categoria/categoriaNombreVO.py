from domain.rules.categoria.categoriaNombreLimite import CategoriaNombreLimite


class CategoriaNombreVO:
    def CategoriaNombre(self, nombre):
        return CategoriaNombreLimite.applyRule(self, nombre)