from django.db import models


# Idioma
# Clase que define un idioma.
class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    habilitado = models.BooleanField(default=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre
