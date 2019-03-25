from django.db import models


# Categoria
# Clase que define una categoria de libros.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    habilitado = models.BooleanField(default=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre
