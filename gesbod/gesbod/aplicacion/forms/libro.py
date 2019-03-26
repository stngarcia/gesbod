from django.forms import ModelForm
from gesbod.aplicacion.models.libro import Libro


# LibroCreateForm
# Formulario de creación de libros.
class LibroCreateForm(ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'isbn', 'autor', 'editorial', 'categoria', 'idioma', 'sinopsis')


# LibroUpdateForm
# Formulario de edición de libros.
class LibroUpdateForm(ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'isbn', 'autor', 'editorial', 'categoria', 'idioma', 'sinopsis', 'disponible')
