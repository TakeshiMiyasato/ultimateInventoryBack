class ProductoDescripcionLimite:
    def applyRule(self, descripcion):
        if len(descripcion) > 200:
            raise Exception('La descripcion no debe superar los 200 caracteres')
        elif len(descripcion) == 0:
            raise Exception('La descripcion no puede ser vacio')
        else:
            return descripcion
