from domain.model.producto import Producto
from domain.repositories.producto.productoRepository import ProductoRepository


class ProductoFactory:
    def createProducto(self, request):
        return Producto(request)