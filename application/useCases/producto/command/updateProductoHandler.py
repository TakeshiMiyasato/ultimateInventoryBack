from application.useCases.producto.command.crearProductoCommand import CrearProductoCommand
from application.useCases.producto.command.updateProductoCommand import UpdateProductoCommand
from domain.repositories.producto.productoRepository import ProductoRepository


class UpdateProductoHandler:
    def updateProducto(self, request):
        obj_producto = UpdateProductoCommand.updateProductoCommand(self, request)
        return ProductoRepository.updateProducto(self, request, obj_producto)