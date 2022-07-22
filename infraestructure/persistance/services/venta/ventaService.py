from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response

from infraestructure.models import Producto, DetalleVenta, Venta, Stock


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'


class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ('id', 'venta', 'producto_nombre', 'cantidad', 'precioVenta', 'producto')


class VentaService:
    def saveVenta(self, obj_venta):
        obj_venta.save()
        serializer = VentaSerializer(obj_venta, many=False)
        return Response(serializer.data)

    def createDetalleVenta(self, obj_detalleVenta):
        obj_detalleVenta.save()
        serializer = DetalleVentaSerializer(obj_detalleVenta, many=False)
        return Response(serializer.data)

    def getVentasByUser(self, request):
        ventas = Venta.objects.all().filter(usuario_id=request.data['id']).order_by('-fecha')
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data)

    def getVentaById(self, request):
        response = {"detalleVentas": [], "venta": {}}
        venta = Venta.objects.get(pk=request.data['id'])
        detalleVentas = DetalleVenta.objects.all().filter(venta_id=request.data['id'])
        serializerDetalleVentas = DetalleVentaSerializer(detalleVentas, many=True)
        serializerVenta = VentaSerializer(venta, many=False)
        response["detalleVentas"] = serializerDetalleVentas.data
        response["venta"] = serializerVenta.data
        return Response(response)

    def getVentasPendientes(self, request):
        ventas = Venta.objects.all().order_by('estado').filter(estado__in=[0, 1, 2])
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data)

    def getVentasAnuladasRechazadas(self, request):
        ventas = Venta.objects.all().order_by('estado').filter(estado__in=[4, 5])
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data)

    def getVentasEntregadas(self, request):
        ventas = Venta.objects.all().order_by('estado').filter(estado__in=[3])
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data)

    ##############################################################

    def creadoPagado(self, request, pk=None):
        venta = get_object_or_404(Venta, pk=request.data['id'])
        venta.estado_creado_pagado()
        venta.save()
        serializer = VentaSerializer(venta, many=False)
        return Response(serializer.data)

    def pagadoAceptado(self, request, pk=None):
        venta = get_object_or_404(Venta, pk=request.data['id'])
        venta.estado_pagado_aceptado()
        venta.save()
        serializer = VentaSerializer(venta, many=False)
        return Response(serializer.data)

    def pagadoRechazado(self, request, pk=None):
        venta = get_object_or_404(Venta, pk=request.data['id'])

        serializer = VentaSerializer(venta, many=False)

        detallesVenta = DetalleVenta.objects.filter(venta_id=venta.id)
        serializer2 = DetalleVentaSerializer(detallesVenta, many=True)

        for x in serializer2.data:
            stock = Stock()
            stock.stockActual = Stock.objects.filter(producto_id=x['producto']).last().stockActual + x['cantidad']
            stock.agregado = x['cantidad']
            stock.emitido = 0
            stock.producto_id = x['producto']
            stock.save()

        venta.estado_pagado_rechazado()
        venta.save()
        return Response(serializer.data)

    def aceptadoEntregado(self, request, pk=None):
        venta = get_object_or_404(Venta, pk=request.data['id'])
        venta.estado_aceptado_entregado()
        venta.save()
        serializer = VentaSerializer(venta, many=False)
        return Response(serializer.data)

    def anular(self, request, pk=None):
        venta = get_object_or_404(Venta, pk=request.data['id'])

        serializer = VentaSerializer(venta, many=False)

        detallesVenta = DetalleVenta.objects.filter(venta_id=venta.id)
        serializer2 = DetalleVentaSerializer(detallesVenta, many=True)

        for x in serializer2.data:
            stock = Stock()
            stock.stockActual = Stock.objects.filter(producto_id=x['producto']).last().stockActual + x['cantidad']
            stock.agregado = x['cantidad']
            stock.emitido = 0
            stock.producto_id = x['producto']
            stock.save()

        venta.estado_anular()
        venta.save()
        return Response(serializer.data)
