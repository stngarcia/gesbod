from django.forms import ModelForm
from gesbod.aplicacion.models.libro import Libro,  AgregarEjemplar


# LibroForm
# Formulario de libros.
class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'isbn', 'autor', 'editorial',
                  'categoria', 'idioma', 'sinopsis')


# AgregarEjemplarForm
# Formulario para agregar ejemplares de libros.
class AgregarEjemplarForm(ModelForm):
    class Meta:
        model = AgregarEjemplar
        fields = ('orden_compra', 'cantidad_ejemplares')
