from django.db import models


# Categoria
# Clase que define una categoria de libros.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    habilitado = models.BooleanField(default=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# Editorial
# Clase que define una editorial de libros.
class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    habilitado = models.BooleanField(default=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# Autor
# Clase que define un autor.
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    descripcion = models.TextField(
        verbose_name='Reseña', null=True, blank=True, max_length=100)
    habilitado = models.BooleanField(default=True)

    class meta:
        ordering = ('nombre', 'apellidos',)

    def __str__(self):
        return self.nombre


# Sucursal
# Clase que define una sucursal.
class Sucursal(models.Model):
    nombre = models.CharField(max_length=30)
    encargado = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100, verbose_name='Dirección')
    habilitado = models.BooleanField(default=True)

    class meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# Idioma
# Clase que define un idioma.
class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    habilitado = models.BooleanField(default=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# Idioma
# Clase que define un idioma.
class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    iso_code = models.CharField(max_length=5)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# Libro
# Clase que define un libro.
class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    ISBN = models.CharField(max_length=30, verbose_name='ISBN')
    autor = models.ForeignKey(
        'Autor', on_delete=models.SET_NULL, null=True, help_text='Seleccione un autor')
    editorial = models.ForeignKey(
        'Editorial', on_delete=models.SET_NULL, null=True, help_text='Seleccione una editorial')
    categoria = models.ManyToManyField(
        Categoria, help_text='Seleccione una categoría')
    idioma = models.ForeignKey(
        'Idioma', on_delete=models.SET_NULL, null=True, help_text='Seleccione un idioma')
    sinopsis = models.TextField(
        max_length=1000, null=True, blank=True, help_text='Ingrese la sinopsis')
    habilitado = models.BooleanField(default=True)

    class meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre
