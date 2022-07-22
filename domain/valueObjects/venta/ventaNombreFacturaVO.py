from domain.rules.venta.ventaNombreFacturaLimite import VentaNombreFacturaLimite
from domain.rules.venta.ventaNombreFacturaRestriccionCaracteres import VentaNombreFacturaRestriccionCaracteres


class VentaNombreFacturaVO:
    def VentaNombreFactura(self, nombre_factura):
        self.nombre_factura = VentaNombreFacturaLimite.appyRule(self, nombre_factura)
        self.nombre_factura = VentaNombreFacturaRestriccionCaracteres.appyRule(self, nombre_factura)
        return self.nombre_factura