from rest_framework.response import Response

from domain.valueObjects.venta.ventaNitVO import VentaNitVO
from domain.valueObjects.venta.ventaNombreFacturaVO import VentaNombreFacturaVO


class Venta:
    def __init__(self, request):
        if request['nombre_factura'] != "" and request['nit_factura'] != 0:
            self.nombre_factura = VentaNombreFacturaVO.VentaNombreFactura(self, request['nombre_factura'])
            self.nit_factura = VentaNitVO.VentaNit(self, request['nit_factura'])
        elif request['nombre_factura'] == "" and request['nit_factura'] != 0:
            Response('No puede haber nit sin nombre')
            raise Exception('No puede haber nit sin nombre')
        elif request['nombre_factura'] == "" and request['nit_factura'] == 0:
            self.nombre_factura = "Sin Nombre"
            self.nit_factura = 0
        else:
            self.nombre_factura = VentaNombreFacturaVO.VentaNombreFactura(self, request['nombre_factura'])
            self.nit_factura = 0

        self.usuario = request['usuario']

