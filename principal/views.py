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
from principal.forms import  RolForm, asignarForm
from principal.forms import UserForm, UserProfileForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User, Group
# Create your views here.
#from principal.models import Rol



def home(request):
    """
    Vista que genera el index
    @param request: Peticion HTTP
    @return: Renderiza la pagina correspondiente
    """
    return render_to_response('index.html', context_instance=RequestContext(request))


def ingresar(request):
    """
    Login
    @param request: Peticion HTTP
    @return: Renderiza el form correspondiente
    """
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/home')
    if request.method == 'POST':

        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/home')
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
    """
    Metodo para cerrar la sesion
    @param request: Peticion HTTP
    @return: Retorna al index
    """
    logout(request)
    return HttpResponseRedirect('/')


def user_profile(request):
    """
    Almacena el perfil de un usuario
    @param request: Peticion HTTP
    @return: El form correspondiente
    """
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






def admin_rol(request):
    """
    Renderiza la pagina de administracion de roles
    @param request: Peticion HTTP
    @return: pagina de adminsitracion de proyectos
    """
    lista_roles = Group.objects.all()
    for rol in lista_roles:
        rol.url = rol.name.replace(' ', '_')

    #return render(request, "admin_roles.html", )
    return render_to_response('admin_roles.html', {'roles': lista_roles}, context_instance=RequestContext(request))


def add_rol(request):
    """
    Renderiza la pagina de agregar roles
    @param request: Peticion HTTP
    @return: pagina de agregar roles
    """
 # Obtener el contexto del request.
    context = RequestContext(request)
    # es POST?
    if request.method == 'POST':
        form = RolForm(request.POST)
        # el form es valido?
        if form.is_valid():
            # guardar
            form.save(commit=True)
            return admin_rol(request)
        else:
            # hubo errores
            print form.errors
    else:
        # si no fue un post, mostrar el form
        form = RolForm()
    return render_to_response('add_rol.html', {'form': form}, context)


def edit_rol(request, rol_name):
    context = RequestContext(request)
    try:
        rol = Group.objects.get(name=rol_name)
        print rol.name
        form = RolForm(instance=rol)
        if form.is_valid():
            print 'form valido'
            rol = form.save(commit=False)
            rol.save()
            return admin_rol(request)
        else:
            print 'form no valido'
            print form.errors

    except Group.DoesNotExist:
        pass
    return render_to_response('add_rol.html', {'form': form}, context)


def asignar_rol(request):
    """
    Pagina de asignacion de roles a usuarios
    @param request: Peticion HTTP
    @return: pagina de asignacion de roles a usuarios
    """
 # Obtener el contexto del request.
    context = RequestContext(request)
    # es POST?
    if request.method == 'POST':
        form = asignarForm(request.POST)
        if form.is_valid():
            # guardar
            idUser = request.POST.__getitem__('username')
            listidGroup = request.POST.__getitem__('groups')
            user = User.objects.get(id=idUser)
            grupos = []
            for idG in listidGroup:
                mygroup = Group.objects.get(id=idG)
                grupos.append(mygroup);

            user.groups = grupos
            return admin_rol(request)
        else:
            # hubo errores
            print form.errors
    else:
        # si no fue un post, mostrar el form
        form = asignarForm()
    return render_to_response('asignar_rol.html', {'form': form}, context)

def admin_usuario(request):
    """
    Renderiza la pagina de administracion de usuario
    @param request: Peticion HTTP
    @return: el form correspondiente
    """
    lista = User.objects.all()
    # for u in lista (
    #     u
    # )
    return render_to_response('admin_usuarios.html', {'lista': lista}, context_instance=RequestContext(request))