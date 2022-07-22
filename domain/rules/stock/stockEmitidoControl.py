class StockEmitidoControl:
    def applyRule(self, agregado, emitido):
        if agregado > 0 and emitido > 0:
            raise Exception('No se puede agregar y emitir en el mismo transaction')
        elif agregado == 0 and emitido == 0:
            raise Exception('No puede haber transaction si no se ha movido nada')
        else:
            return emitido