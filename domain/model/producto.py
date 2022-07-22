from domain.rules.producto.productoCategoriaExiste import ProductoCategoriaExiste
from domain.rules.producto.productoDescripcionLimite import ProductoDescripcionLimite
from domain.rules.producto.productoNombreLimite import ProductoNombreLimite
from domain.rules.producto.productoPrecioLimite import ProductoPrecioLimite
from domain.valueObjects.producto.productoCategoriaVO import ProductoCategoriaVO
from domain.valueObjects.producto.productoDescripcionVO import ProductoDescripcionVO
from domain.valueObjects.producto.productoNombreVO import ProductoNombreVO
from domain.valueObjects.producto.productoPrecioVO import ProductoPrecioVO


class Producto:
    def __init__(self, request):
        self.nombre = ProductoNombreVO.ProductoNombre(self, request.data['nombre'])
        self.descripcion = ProductoDescripcionVO.ProductoDescripcion(self, request.data['descripcion'])
        self.precio = ProductoPrecioVO.ProductoPrecio(self, request.data['precio'])
        self.categoria = ProductoCategoriaVO.ProductoCategoria(self, request.data['categoria'])