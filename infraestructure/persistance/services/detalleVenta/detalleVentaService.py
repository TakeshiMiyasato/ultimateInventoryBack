# from rest_framework import serializers
# from rest_framework.response import Response
#
# from infraestructure.models import DetalleVenta
#
#
# class DetalleVentaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DetalleVenta
#         fields = ('id', 'venta', 'producto_nombre', 'cantidad', 'precioVenta', 'producto')

# INUTILIZADO POR VENTA SERVICE, AHORA LO TRAE EN FORMA DE AGREGADO


# class DetalleVentaService:
#     def getDetalleVentasByVenta(self, request):
#         detalleVentas = DetalleVenta.objects.all().filter(venta_id=request.data['idVenta'])
#         serializer = DetalleVentaSerializer(detalleVentas, many=True)
#         return Response(serializer.data)
