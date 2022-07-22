from django.db.models.signals import pre_save
from django.dispatch import receiver

from domain.model.producto import Producto


@receiver(pre_save, sender=Producto)
def my_handler(sender, **kwargs):
    print('////////////////////////////////////////////////////////////////////////////////')