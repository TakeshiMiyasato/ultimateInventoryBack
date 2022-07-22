from domain.factories.producto.productoFactory import ProductoFactory


class CrearProductoCommand:
    def crearProductoCommand(self, request):
        return ProductoFactory.createProducto(self, request)