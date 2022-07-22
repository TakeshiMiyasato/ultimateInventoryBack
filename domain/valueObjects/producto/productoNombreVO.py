from domain.rules.producto.productoNombreLimite import ProductoNombreLimite


class ProductoNombreVO:
    def ProductoNombre(self, nombre):
        return ProductoNombreLimite.applyRule(self, nombre)