from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Formulario de inicio de sesion.
class IniciarSesionForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(), label="Nombre de Usuario")
    password = forms.CharField(
        widget=forms.PasswordInput(), label="Contraseña")


class registrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'is_superuser', 'is_active', 'username')
