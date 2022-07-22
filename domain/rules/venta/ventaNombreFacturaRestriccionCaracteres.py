import re


class VentaNombreFacturaRestriccionCaracteres:
    def appyRule(self, nombre):
        if re.match('^[a-z\dA-Z]*$', nombre):
            return nombre
        else:
            raise Exception('El nombre contiene Numeros o caracteres especiales')