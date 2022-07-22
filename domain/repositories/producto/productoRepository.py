from domain.model.producto import Producto
from infraestructure.persistance.services.producto.productoService import ProductoService
from shareKernel.core.EventHandler import EventHandler

event_handler = EventHandler()

class ProductoRepository:
    def getAllProductos(self, request):
        return ProductoService.getAllProductos(self, request)

    def getProductoById(self, request):
        return ProductoService.getProductoById(self, request)

    def getProductosByCategoria(self, request):
        return ProductoService.getProductosByCategoria(self, request)

    def createProducto(self, request):
        return ProductoService.createProducto(self, request, event_handler)

    def updateProducto(self, request, obj_producto):
        return ProductoService.updateProducto(self, request, obj_producto, event_handler)