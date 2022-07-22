from datetime import datetime

from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(null=False, max_length=200)
    fechaCreacion =models.DateTimeField(default=datetime.now, blank=True)
    fechaLastUpdate =models.DateTimeField(default=datetime.now, blank=True)
