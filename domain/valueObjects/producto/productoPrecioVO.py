from domain.rules.producto.productoPrecioLimite import ProductoPrecioLimite


class ProductoPrecioVO:
    def ProductoPrecio(self, precio):
        return ProductoPrecioLimite.applyRule(self, precio)