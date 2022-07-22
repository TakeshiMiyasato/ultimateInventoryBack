from rest_framework.response import Response

from domain.factories.producto.productoFactory import ProductoFactory
from infraestructure.models import Venta, DetalleVenta, Stock
from infraestructure.persistance.services.stock.stockService import StockService
from infraestructure.persistance.services.venta.ventaService import VentaSerializer, DetalleVentaSerializer, \
    VentaService


class CrearVentaCommand:
    def crearVentaCommand(self, obj_venta, arr_detalleVentas):
        arrayDetalleVentas = []
        array = {"detallesVenta": [], "venta": {}}
        total = 0

        venta = Venta()
        venta.nombre_factura = obj_venta.nombre_factura
        venta.nit_factura = obj_venta.nit_factura
        venta.usuario_id = obj_venta.usuario
        venta.save()
        serializerVenta = VentaSerializer(venta, many=False)

        for x in arr_detalleVentas:
            detalleVenta = DetalleVenta()
            detalleVenta.producto_id = x.producto
            detalleVenta.venta_id = venta.id
            detalleVenta.cantidad = x.cantidad
            detalleVenta.precioVenta = x.precioVenta
            VentaService.createDetalleVenta(self, detalleVenta)
            serializer = DetalleVentaSerializer(detalleVenta, many=False)
            arrayDetalleVentas.append(serializer.data)
            total += detalleVenta.precioVenta

            stock = Stock()
            stock.producto_id = x.producto
            stock.agregado = 0
            stock.emitido = x.cantidad
            stock.stockActual = Stock.objects.filter(producto_id=x.producto).last().stockActual - x.cantidad
            StockService.crearRegistroStock(self, stock)

        venta.total = total
        VentaService.saveVenta(self, venta)
        array["detallesVenta"] = arrayDetalleVentas

        array["venta"] = serializerVenta.data

        return Response(array)