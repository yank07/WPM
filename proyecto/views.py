"""
Creado el 1 abril  2014
@author: Grupo 04
"""

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from proyecto.forms import ProyectoForm
from principal.forms import UserForm, UserProfileForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User, Group
# Create your views here.
#from principal.models import Rol
from proyecto.models import Proyecto
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def admin_proyecto(request):
    """
    Renderiza la pagina de proyectos
    @param request: Peticion HTTP
    @return: el form correspondiente
    """
    lista = Proyecto.objects.all()
    return render_to_response('admin_proyectos.html', {'lista': lista}, context_instance=RequestContext(request))

@login_required
def add_proyecto(request):
    """
    Vista para agregar un proyecto.
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    # Obtener el contexto del request.
    context = RequestContext(request)
    # es POST?
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        # el form es valido?
        if form.is_valid():
            # guardar
            form.save(commit=True)
            return admin_proyecto(request)
        else:
            # hubo errores
            print form.errors
    else:
        # si no fue un post, mostrar el form
        form = ProyectoForm()
    return render_to_response('add_proyecto.html', {'form': form}, context)


