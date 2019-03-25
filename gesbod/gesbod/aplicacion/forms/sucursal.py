from django.forms import ModelForm
from gesbod.aplicacion.models import Sucursal


# SucursalForm
# Formulario de sucursales.
class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ('nombre', 'encargado', 'direccion', 'habilitado')
