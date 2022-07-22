from django.db.models.signals import pre_save
from django.dispatch import receiver

from domain.factories.venta.ventaFactory import VentaFactory
from infraestructure.models import Venta


@receiver(pre_save, sender=Venta)
def my_handler(sender, **kwargs):
    print('////////////////////////////////////////////////////////////////////////////////')
