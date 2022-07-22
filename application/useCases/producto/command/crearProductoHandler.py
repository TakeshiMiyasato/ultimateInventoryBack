from application.useCases.producto.command.crearProductoCommand import CrearProductoCommand
from domain.repositories.producto.productoRepository import ProductoRepository


class CrearProductoHandler:
    def crearProducto(self, request):
        obj_producto = CrearProductoCommand.crearProductoCommand(self, request)
        return ProductoRepository.createProducto(self, obj_producto)