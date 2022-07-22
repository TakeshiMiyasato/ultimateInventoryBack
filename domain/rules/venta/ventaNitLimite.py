class VentaNitLimite:
    def applyRule(self, nit):
        if len(str(nit)) > 10:
            raise Exception('El nit no puede tener mas de 10 caracteres')
        elif len(str(nit)) < 7:
            raise Exception('el nit no puede tener menos de 7 caracteres')
        elif nit == 0:
            return nit
        else:
            return nit