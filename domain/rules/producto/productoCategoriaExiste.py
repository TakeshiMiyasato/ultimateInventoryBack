from infraestructure.models import Categoria


class ProductoCategoriaExiste:
    def applyRule(self, categoria_id):
        categoria = Categoria.objects.get(pk=categoria_id)
        if categoria is None:
            raise Exception('La categoria no existe')
        else:
            return categoria_id