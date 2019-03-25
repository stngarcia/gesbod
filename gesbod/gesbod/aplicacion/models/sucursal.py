from django.db import models


# Sucursal
# Clase que define una sucursal.
class Sucursal(models.Model):
    nombre = models.CharField(max_length=30)
    encargado = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100, verbose_name='Dirección')
    habilitado = models.BooleanField(default=True)

    class meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre
