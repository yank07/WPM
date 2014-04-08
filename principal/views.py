from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal.forms import ProyectoForm
from django.contrib.auth.models import User
# Create your views here.


def home(request):

    return render_to_response('index.html', context_instance=RequestContext(request))


def admin_proyecto(request):
    return render_to_response('admin_proyectos.html', context_instance=RequestContext(request))


def add_proyecto(request):
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