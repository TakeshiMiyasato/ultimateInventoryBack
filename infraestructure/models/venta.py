from django.contrib.auth.models import User
from django.db import models
from django_fsm import FSMIntegerField, transition


class Venta(models.Model):
    CREADO = 0
    PAGADO = 1
    PAGO_ACEPTADO = 2
    ENTREGADO = 3
    PAGO_RECHAZADO = 4
    ANULADO = 5

    ESTADO_CHOISES = (
        (CREADO, 'Creado'),
        (PAGADO, 'Pagado'),
        (PAGO_ACEPTADO, 'Pago Aceptado'),
        (ENTREGADO, 'Entregado'),
        (PAGO_RECHAZADO, 'Pago Rechazado'),
        (ANULADO, 'Anulado')
    )

    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    estado = FSMIntegerField(choices=ESTADO_CHOISES, protected=True, default=0)
    total = models.IntegerField(default=0)
    nombre_factura = models.CharField(max_length=200, default='Sin nombre')
    nit_factura = models.IntegerField(default=0, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='venta_usuario')

    @transition(field=estado, source=CREADO, target=PAGADO)
    def estado_creado_pagado(self):
        pass

    @transition(field=estado, source=PAGADO, target=PAGO_ACEPTADO)
    def estado_pagado_aceptado(self):
        pass

    @transition(field=estado, source=PAGADO, target=PAGO_RECHAZADO)
    def estado_pagado_rechazado(self):
        pass

    @transition(field=estado, source=PAGO_ACEPTADO, target=ENTREGADO)
    def estado_aceptado_entregado(self):
        pass

    @transition(field=estado, source=[CREADO, PAGADO, PAGO_RECHAZADO, PAGO_ACEPTADO], target=ANULADO)
    def estado_anular(self):
        pass
