from django.conf.urls import url
from gesbod.aplicacion.views import inicio, login, usuarios


urlpatterns = [
    # Rutas de la pantalla de inicio.
    url(r'^$', inicio.irInicio, name='irInicio'),

    # Rutas de las sesiones.
    url(r'^iniciarSesion/$', login.iniciarSesion, name='iniciarSesion'),
    url(r'^cerrarSesion/$', login.cerrarSesion, name='cerrarSesion'),
    url(r'^denegarAcceso/$', login.denegarAcceso, name='denegarAcceso'),
    url(r'^restringirAcceso/$', login.restringirAcceso, name='restringirAcceso'),

    # Rutas para las cuentas de usuario.
    url(r'^usuarios/$', usuarios.ListaDeUsuarios.as_view(), name='listaDeUsuarios'),
    url(r'^registrar/$', usuarios.RegistrarUsuario.as_view(), name='registrarUsuario'),
    url(r'^editarUsuario/(?P<pk>\d+)$',
        usuarios.EditarUsuario.as_view(), name='editarUsuario'),
    url(r'^eliminarUsuario/(?P<pk>\d+)$',
        usuarios.EliminarUsuario.as_view(), name='eliminarUsuario'),
    url(r'^verUsuario/(?P<pk>\d+)$',
        usuarios.VerUsuario.as_view(), name='verUsuario'),
]
