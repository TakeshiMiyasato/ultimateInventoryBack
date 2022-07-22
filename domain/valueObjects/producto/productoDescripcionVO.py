from domain.rules.producto.productoDescripcionLimite import ProductoDescripcionLimite


class ProductoDescripcionVO:
    def ProductoDescripcion(self, descripcion):
        return ProductoDescripcionLimite.applyRule(self, descripcion)