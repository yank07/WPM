"""
Creado el 1 abril  2014
@author: Grupo 04
"""

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from principal.forms import ProyectoForm
from principal.forms import UserForm, UserProfileForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def ingresar(request):
    """
    Login
    @param request: Peticion HTTP
    @return: Renderiza el form correspondiente
    """
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/admin_proyectos')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/admin_proyectos')
                else:
                    return render_to_response('no_activo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('no_usuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html', {'formulario': formulario}, context_instance=RequestContext(request))


def nuevo_usuario(request):
    """
    Metodo para crear un usuario
    @param request: Peticion HTTP
    @return: Renderiza el form correspondiente
    """

    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/nuevo_usuario/perfil')
    else:
        formulario = UserCreationForm()

    return render_to_response('nuevo_usuario.html',{'formulario':formulario},context_instance=RequestContext(request))


def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_profile(request):
    if request.method == 'POST':
        formulario = UserProfileForm(request.POST, instance= User.objects.last().profile)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        user= request.user
        profile = user.profile
        formulario = UserProfileForm(instance=profile)
    args = {}
    args.update(csrf(request))
    args['formulario']= formulario
    return render_to_response('perfil.html', args, context_instance=RequestContext(request))



def admin_proyecto(request):
    return render_to_response('admin_proyectos.html', context_instance=RequestContext(request))


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


