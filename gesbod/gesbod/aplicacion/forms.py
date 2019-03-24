from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Editorial, Categoria, Autor


# IniciarSesionForm
# Formulario de autores.
class IniciarSesionForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(), label="Nombre de Usuario")
    password = forms.CharField(
        widget=forms.PasswordInput(), label="Contraseña")


# UsuarioForm
# Formulario de usuarios.
class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'is_superuser', 'is_active', 'username')


# EditorialForm
# Formulario de editoriales.
class EditorialForm(ModelForm):
    class Meta:
        model = Editorial
        fields = ('nombre', 'habilitado')


# CategoriaForm
# Formulario de categorias.
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre', 'habilitado')


# AutorForm
# Formulario de autores.
class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre', 'apellidos', 'descripcion', 'habilitado')
