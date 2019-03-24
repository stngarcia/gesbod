from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Editorial

# Formulario de inicio de sesion.


class IniciarSesionForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(), label="Nombre de Usuario")
    password = forms.CharField(
        widget=forms.PasswordInput(), label="Contraseña")


class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'is_superuser', 'is_active', 'username')


class EditorialForm(ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre']