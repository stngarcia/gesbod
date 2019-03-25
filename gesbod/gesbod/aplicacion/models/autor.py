from django.db import models


# Autor
# Clase que define un autor.
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    descripcion = models.TextField(
        verbose_name='Reseña', null=True, blank=True, max_length=100)
    habilitado = models.BooleanField(default=True)

    class meta:
        ordering = ('nombre', 'apellidos',)

    def __str__(self):
        return self.nombre
