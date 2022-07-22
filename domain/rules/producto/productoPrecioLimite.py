class ProductoPrecioLimite:
    def applyRule(self, precio):
        if int(precio) > 2000:
            raise Exception('El precio no debe superar los 2000.00')
        elif int(precio) == 0:
            raise Exception('El precio no debe ser 0')
        else:
            return precio