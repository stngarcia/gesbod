import uuid
from django.db import models
from gesbod.aplicacion.models import autor, categoria, idioma, editorial, sucursal
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


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
    cantidad_ejemplares = models.PositiveIntegerField(
        default=0, verbose_name='Cantidad de ejemplares', validators=[MaxValueValidator(999)])

    class meta:
        ordering = ('titulo',)

    def get_absolute_url(self):
        return reverse('verLibro', args=[self.id])

    def get_update_url(self):
        return reverse('editarLibro', args=[self.id])

    def get_delete_url(self):
        return reverse('eliminarLibro', args=[self.id])

    def get_add_instance_url(self):
        return reverse('agregarEjemplar', args=[self.id])

    def get_list_instance_url(self):
        return reverse('listarEjemplares', args=[self.id])

    def __str__(self):
        return self.titulo


# AgregarEjemplar
# Clase para agregar ejemplares de libros.
class AgregarEjemplar(models.Model):
    orden_compra = models.CharField(
        max_length=25, null=True, blank=True, help_text='Ingrese nro. orden de compra')
    cantidad_ejemplares = models.IntegerField(
        default=1, verbose_name='Cantidad de ejemplares', validators=[MaxValueValidator(99), MinValueValidator(1)])


# Ejemplar
# Clase que define un ejemplar de un libro.
class Ejemplar_libro(models.Model):
    ESTADO_LIBRO = (
        ('v', 'Vendido'), ('d', 'Disponible'), ('r', 'Reservado'),)

    retiro_LIBRO = (
        ('t', 'Tienda'), ('d', 'Domicilio'))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Identificador del ejemplar')
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
    orden_compra = models.CharField(
        max_length=25, null=True, blank=True, help_text='Ingrese nro. orden de compra')
    estado = models.CharField(max_length=1, choices=ESTADO_LIBRO,
                              blank=True, default='d', help_text='Seleccione estado')
    sucursal = models.ForeignKey(
        sucursal.Sucursal, on_delete=models.SET_NULL, null=True, help_text='Seleccione una sucursal')
    nombre_cliente = models.CharField(
        max_length=50, null=True, blank=True, help_text='Ingrese cliente que reserva el libro')
    retirar_en = models.CharField(max_length=1, choices=ESTADO_LIBRO,
                                  blank=True, default='t', help_text='Retirar en')
    direccion_retiro = models.CharField(
        max_length=100, null=True, blank=True, help_text='Ingrese dirección de retiro')