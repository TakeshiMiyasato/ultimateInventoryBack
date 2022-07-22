from django.db.models.signals import pre_save
from django.dispatch import receiver

from domain.factories.stock.stockFactory import StockFactory
from infraestructure.models import Stock


@receiver(pre_save, sender=Stock)
def my_handler(sender, **kwargs):
    print('////////////////////////////////////////////////////////////////////////////////')