import os

from application.useCases.categoria.command.crearCategoriaHandler import CrearCategoriaHandler
from application.useCases.categoria.command.updateCategoriaHandler import UpdateCategoriaHandler
from application.useCases.producto.command.crearProductoHandler import CrearProductoHandler
from application.useCases.producto.command.updateProductoHandler import UpdateProductoHandler
from application.useCases.stock.command.actualizarStockHandler import ActualizarStockHandler
from application.useCases.venta.command.crearVentaHandler import CrearVentaHandler
# from domain.events.producto.productoEvents import ProductoEvents
# from domain.events.stock.stockEvents import StockEvents
# from domain.events.venta.ventaEvents import VentaEvents
from domain.repositories.categoria.categoriaRepository import CategoriaRepository
# from domain.repositories.detalleVenta.detalleVentaRepository import DetalleVentaRepository
from domain.repositories.producto.productoRepository import ProductoRepository
from domain.repositories.stock.stockRepository import StockRepository
from domain.repositories.venta.ventaRepository import VentaRepository


class Mediator:
    def WriteDb(self, request, action):
        if action == 'createCategoria':
            return CrearCategoriaHandler.crearCategoria(self, request)
        elif action == 'updateCategoria':
            return UpdateCategoriaHandler.updateCategoria(self, request)
        elif action == 'createProducto':
            return CrearProductoHandler.crearProducto(self, request)
        elif action == 'updateProducto':
            return UpdateProductoHandler.updateProducto(self, request)
        elif action == 'actualizarStock':
            return ActualizarStockHandler.actualizarStock(self, request)
        elif action == 'createVenta':
            return CrearVentaHandler.crearVenta(self, request)
        elif action == 'creadoPagado':
            return VentaRepository.creadoPagado(self, request)
        elif action == 'pagadoAceptado':
            return VentaRepository.pagadoAceptado(self, request)
        elif action == 'pagadoRechazado':
            return VentaRepository.pagadoRechazado(self, request)
        elif action == 'aceptadoEntregado':
            return VentaRepository.aceptadoEntragado(self, request)
        elif action == 'anular':
            return VentaRepository.anular(self, request)

    def ReadDb(self, request, action):
        if action == 'getAllCategorias':
            return CategoriaRepository.getAllCategorias(self, request)
        if action == 'getCategoriaById':
            return CategoriaRepository.getCategoriaById(self, request)
        # elif action == 'getDetalleVentasByVenta':
        #     return DetalleVentaRepository.getDetalleVentasByVenta(self, request)
        elif action == 'getAllProductos':
            return ProductoRepository.getAllProductos(self, request)
        elif action == 'getProductoById':
            return ProductoRepository.getProductoById(self, request)
        elif action == 'getProductosByCategoria':
            return ProductoRepository.getProductosByCategoria(self, request)
        elif action == 'getStockByProducto':
            return StockRepository.getStockByProducto(self, request)
        elif action == 'getHistorialByProducto':
            return StockRepository.getHistorialByProducto(self, request)
        elif action == 'getVentasByUser':
            return VentaRepository.getVentasByUser(self, request)
        elif action == 'getVentaById':
            return VentaRepository.getVentaById(self, request)
        elif action == 'getVentasPendientes':
            return VentaRepository.getVentasPendientes(self, request)
        elif action == 'getVentasAnuladasRechazadas':
            return VentaRepository.getVentasAnuladasRechazadas(self, request)
        elif action == 'getVentasEntregadas':
            return VentaRepository.getVentasEntregadas(self, request)
