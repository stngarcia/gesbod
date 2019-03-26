import operator
from django.conf import settings
from functools import reduce
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from gesbod.aplicacion.models.libro import Libro
from gesbod.aplicacion.forms.libro import LibroCreateForm, LibroUpdateForm


# ListaDeLibros
# Clase que permite el listado de los libros del sistema.
class ListaDeLibros(ListView):
    model = Libro
    template_name = 'libros/listaDeLibros.html'
    paginate_by = settings.REGISTROS_POR_PAGINA

    def get_queryset(self):
        result = super(ListaDeLibros, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(reduce(operator.and_,
                                          (Q(titulo__icontains=q) for q in query_list)) |
                                   reduce(operator.and_, (Q(titulo__icontains=q)
                                                          for q in query_list))
                                   )
        return result


# VerLibro
# Clase que permite visualizar la informacion de un libro.
class VerLibro(DetailView):
    model = Libro
    template_name = 'libros/verLibro.html'


# RegistrarLibro
# Clase que permite registrar un nuevo libro.
class RegistrarLibro(CreateView):
    model = Libro
    template_name = 'libros/registrarLibro.html'
    form_class = LibroCreateForm
    success_url = reverse_lazy('listaDeLibros')


# EditarLibro
# Clase que permite editar la informacion de un libro.
class EditarLibro(UpdateView):
    model = Libro
    form_class = LibroUpdateForm
    template_name = 'libros/editarLibro.html'
    success_url = reverse_lazy('listaDeLibros')


# EliminarLibro
# Clase que permite eliminar un libro.
class EliminarLibro(DeleteView):
    model = Libro
    template_name = 'libros/eliminarLibro.html'
    success_url = reverse_lazy('listaDeLibros')
