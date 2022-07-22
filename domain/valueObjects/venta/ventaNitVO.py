from domain.rules.venta.ventaNitLimite import VentaNitLimite


class VentaNitVO:
    def VentaNit(self, nit):
        return VentaNitLimite.applyRule(self, nit)