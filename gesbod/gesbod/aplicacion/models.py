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


# Editorial
# Clase que define una editorial de libros.
class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    habilitado = models.BooleanField(default=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# Autor
# Clase que define un autor.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    descripcion = models.TextField(
        verbose_name='Reseña', null=True, blank=True, max_length=250)
    habilitado = models.BooleanField(default=True)

    class meta:
        ordering = ('nombre', 'apellidos',)

    def __str__(self):
        return self.nombre
