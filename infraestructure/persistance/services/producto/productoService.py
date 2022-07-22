from rest_framework import serializers
from rest_framework.response import Response

from infraestructure.models import Producto, Stock


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'descripcion', 'nombre', 'precio', 'categoria_nombre', 'categoria')


class ProductoService:
    def getAllProductos(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def getProductoById(self, request):
        productos = Producto.objects.get(pk=request.data['id'])
        stock = Stock.objects.filter(producto_id=request.data['id']).last().stockActual
        serializer = ProductoSerializer(productos, many=False)
        array = serializer.data
        array['stock'] = stock
        return Response(array)

    def getProductosByCategoria(self, request):
        productos = Producto.objects.filter(categoria_id=request.data['id'])
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def createProducto(self, obj_producto, event_handler):
        producto = Producto()
        producto.nombre = obj_producto.nombre
        producto.precio = obj_producto.precio
        producto.descripcion = obj_producto.descripcion
        producto.categoria_id = obj_producto.categoria
        producto.save()
        stock = Stock()
        stock.producto_id = producto.id
        stock.save()
        serializer = ProductoSerializer(producto, many=False)
        return Response(serializer.data)

    def updateProducto(self, request, obj_producto, event_handler):
        producto = Producto.objects.get(pk=request.data['id'])
        producto.nombre = obj_producto.nombre
        producto.precio = obj_producto.precio
        producto.descripcion = obj_producto.descripcion
        producto.categoria_id = obj_producto.categoria
        producto.save()
        serializer = ProductoSerializer(producto, many=False)
        return Response(serializer.data)
