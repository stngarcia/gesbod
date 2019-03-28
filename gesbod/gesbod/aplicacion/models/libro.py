from django.db import models
from gesbod.aplicacion.models import autor, categoria, idioma, editorial
from django.urls import reverse


# Libro
# Clase que define un libro.
class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    isbn = models.CharField(max_length=30, verbose_name='ISBN')
    autor = models.ForeignKey(
        autor.Autor, on_delete=models.SET_NULL, null=True, help_text='Seleccione un autor')
    editorial = models.ForeignKey(
        editorial.Editorial, on_delete=models.SET_NULL, null=True, help_text='Seleccione una editorial')
    categoria = models.ManyToManyField(
        categoria.Categoria, help_text='Seleccione una categoría')
    idioma = models.ForeignKey(
        idioma.Idioma, on_delete=models.SET_NULL, null=True, help_text='Seleccione un idioma')
    sinopsis = models.TextField(
        max_length=1000, null=True, blank=True, help_text='Ingrese la sinopsis')
    disponible = models.BooleanField(
        default=True, verbose_name='Estado actual')

    class meta:
        ordering = ('titulo',)

    def get_absolute_url(self):
        return reverse('verLibro', args=[self.id])

    def get_update_url(self):
        return reverse('editarLibro', args=[self.id])

    def get_delete_url(self):
        return reverse('eliminarLibro', args=[self.id])

    def __str__(self):
        return self.titulo
