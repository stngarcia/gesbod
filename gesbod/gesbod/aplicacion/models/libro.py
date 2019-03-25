from django.db import models
from gesbod.aplicacion.models import Autor, Categoria, Idioma, Editorial

# Libro
# Clase que define un libro.


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    ISBN = models.CharField(max_length=30, verbose_name='ISBN')
    autor = models.ForeignKey(
        Autor, on_delete=models.SET_NULL, null=True, help_text='Seleccione un autor')
    Editorial = models.ForeignKey(
        Editorial, on_delete=models.SET_NULL, null=True, help_text='Seleccione una editorial')
    categoria = models.ManyToManyField(
        Categoria, help_text='Seleccione una categoría')
    Idioma = models.ForeignKey(
        Idioma, on_delete=models.SET_NULL, null=True, help_text='Seleccione un idioma')
    sinopsis = models.TextField(
        max_length=1000, null=True, blank=True, help_text='Ingrese la sinopsis')
    disponible = models.BooleanField(
        default=True, verbose_name='Estado actual')

    class meta:
        ordering = ('titulo',)

    def __str__(self):
        return self.titulo
