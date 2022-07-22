class ProductoNombreLimite:
    def applyRule(self, nombre):
        if len(nombre) > 100:
            raise Exception('El nombre excede los 100 caracteres')
        elif len(nombre) == 0:
            raise Exception('El nombre no puede estar vacio')
        else:
            return nombre