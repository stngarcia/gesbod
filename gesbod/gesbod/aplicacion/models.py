from django.db import models


# Editorial
# Clase que define una editorial de libros.
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
