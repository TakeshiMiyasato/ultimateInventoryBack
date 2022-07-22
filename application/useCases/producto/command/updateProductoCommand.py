from domain.factories.producto.productoFactory import ProductoFactory


class UpdateProductoCommand:
    def updateProductoCommand(self, request):
        return ProductoFactory.createProducto(self, request)