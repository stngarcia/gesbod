from django.conf.urls import url
from gesbod.aplicacion.views import inicio, login, usuarios, editoriales


urlpatterns = [
    # Rutas de la pantalla de inicio.
    url(r'^$', inicio.irInicio, name='irInicio'),

    # Rutas de las sesiones.
    url(r'^iniciarSesion/$', login.iniciarSesion, name='iniciarSesion'),
    url(r'^cerrarSesion/$', login.cerrarSesion, name='cerrarSesion'),
    url(r'^denegarAcceso/$', login.denegarAcceso, name='denegarAcceso'),
    url(r'^restringirAcceso/$', login.restringirAcceso, name='restringirAcceso'),

    # Rutas para las cuentas de usuario.
    url(r'^lista/usuario/$', usuarios.ListaDeUsuarios.as_view(), name='listaDeUsuarios'),
    url(r'^registrar/usuario/$', usuarios.RegistrarUsuario.as_view(), name='registrarUsuario'),
    url(r'^editar/usuario/(?P<pk>\d+)$',
        usuarios.EditarUsuario.as_view(), name='editarUsuario'),
    url(r'^eliminar/usuario/(?P<pk>\d+)$',
        usuarios.EliminarUsuario.as_view(), name='eliminarUsuario'),
    url(r'^ver/usuario/(?P<pk>\d+)$',
        usuarios.VerUsuario.as_view(), name='verUsuario'),

    # Rutas para las editoriales.
    url(r'^lista/editorial/$', editoriales.ListaDeEditoriales.as_view(), name='listaDeEditoriales'),
    url(r'^registrar/editorial/$', editoriales.RegistrarEditorial.as_view(), name='registrarEditorial'),
    url(r'^editar/editorial/(?P<pk>\d+)$',
        editoriales.EditarEditorial.as_view(), name='editarEditorial'),
    url(r'^eliminar/editorial/(?P<pk>\d+)$',
        editoriales.EliminarEditorial.as_view(), name='eliminarEditorial'),
    url(r'^ver/editorial/(?P<pk>\d+)$',
        editoriales.VerEditorial.as_view(), name='verEditorial'),
]
