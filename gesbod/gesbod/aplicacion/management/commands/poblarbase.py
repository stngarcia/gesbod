from django.contrib.auth.models import User
from gesbod.aplicacion.models.autor import Autor
from gesbod.aplicacion.models.categoria import Categoria
from gesbod.aplicacion.models.editorial import Editorial
from gesbod.aplicacion.models.idioma import Idioma
from gesbod.aplicacion.models.sucursal import Sucursal
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Ingresa valores de prueba para gesbod.'

    def handle(self, *args, **kwargs):
        # Creando usuarios de ejemplo.
        print('Creando usuarios...')
        User.objects.create_superuser(first_name='Daniel', last_name='Garcia Asathor',
                                      username='admin', email='stngarcia8@gmail.com', password='libros_admin')
        User.objects.create_user(first_name='Daniel', last_name='Garcia Asathor',
                                 username='d.garcia', email='stngarcia8@gmail.com', password='libros_user')
        User.objects.create_user(first_name='Elias', last_name='Garcia Carvajal',
                                 username='e.garcia', email='elias@gmail.com', password='libros_user')
        User.objects.create_user(first_name='Hector', last_name='Celis Villarroel',
                                 username='h.celis', email='hector@gmail.com', password='libros_user')
        User.objects.create_user(first_name='Pedro', last_name='Briceño Donoso',
                                 username='p.briceno', email='pedro@gmail.com', password='libros_user')
        User.objects.create_user(first_name='Ignacio', last_name='Salazar Garcia',
                                 username='i.salazar', email='ignacio@gmail.com', password='libros_user')
        # Creando autores de ejemplo.
        print('Creando autores...')
        myAutor = Autor(nombre='Joe', apellidos='Abercrombie',
                        descripcion='', habilitado=True)
        myAutor.save()
        myAutor = Autor(nombre='Dan', apellidos='Abnett',
                        descripcion='', habilitado=True)
        myAutor.save()
        myAutor = Autor(nombre='Graham', apellidos='McNeill',
                        descripcion='', habilitado=True)
        myAutor.save()
        # Creando categorias de ejemplo.
        print('Creando categorias...')
        myCategoria = Categoria(nombre='Ciencia ficción', habilitado=True)
        myCategoria.save()
        myCategoria = Categoria(nombre='Fantasía', habilitado=True)
        myCategoria.save()
        myCategoria = Categoria(nombre='Terror', habilitado=True)
        myCategoria.save()
        # Creando editoriales de ejemplo.
        print('Creando editoriales...')
        myEditorial = Editorial(nombre='Prentice Hall', habilitado=True)
        myEditorial.save()
        myEditorial = Editorial(nombre='Minotauro', habilitado=True)
        myEditorial.save()
        myEditorial = Editorial(nombre='Black library', habilitado=True)
        myEditorial.save()
        # Creando idiomas de ejemplo.
        print('Creando idiomas...')
        myIdioma = Idioma(nombre='Inglés', iso_code='en-us')
        myIdioma.save()
        myIdioma = Idioma(nombre='Español', iso_code='es-es')
        myIdioma.save()
        # Creando sucursales de ejemplo.
        print('Creando sucursales...')
        mySucursal = Sucursal(nombre='Sucursal Plaza Norte', encargado='Ernesto mado',
                              direccion='Plaza norte 1456', habilitado=True)
        mySucursal.save()
        mySucursal = Sucursal(nombre='Sucursal Plaza oeste', encargado='Ana Lisa Melano',
                              direccion='Plaza oeste 6541', habilitado=True)
        mySucursal.save()
        print('Base de datos poblada para pruebas!')
