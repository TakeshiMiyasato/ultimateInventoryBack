class VentaNombreFacturaLimite:
    def appyRule(self, nombre):
        if len(nombre) > 40:
            raise Exception('El nombre en el nit no puede tener mas de 40 letras')
        elif len(nombre) < 2:
            raise Exception('El nombre en el nit no puede tener menos de 2 letras')
        else:
            return nombre