from domain.rules.producto.productoCategoriaExiste import ProductoCategoriaExiste


class ProductoCategoriaVO:
    def ProductoCategoria(self, categoria):
        return ProductoCategoriaExiste.applyRule(self, categoria)