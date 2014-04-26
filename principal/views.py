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
from django_tables2 import RequestConfig
from principal.forms import RolForm, asignarForm, UserEditForm, UserProfileEditForm, UserFilter, GroupFilter
from principal.forms import UserForm, UserProfileForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required
from principal.tables import UserTable, GroupTable
from proyecto.forms import ProyectoFilter
from proyecto.models import Proyecto
from proyecto.tables import ProyectoTable


def home(request):
    """
    Vista que genera el index
    @param request: Peticion HTTP
    @return: Renderiza la pagina correspondiente
    """
    f = ProyectoFilter(request.GET, queryset=request.user.miembros.all())
    lista = ProyectoTable(f)
    RequestConfig(request, paginate={"per_page": 5}).configure(lista)

    return render_to_response('index.html', {'lista': lista, 'filter': f},
                              context_instance=RequestContext(request))


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

@login_required
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

@login_required
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
            return HttpResponseRedirect('/admin_usuarios')
    else:
        user= request.user
        profile = user.profile
        formulario = UserProfileForm(instance=profile)
    args = {}
    args.update(csrf(request))
    args['formulario']= formulario
    return render_to_response('perfil.html', args, context_instance=RequestContext(request))


@login_required
def admin_rol(request):
    """
    Renderiza la pagina de administracion de roles
    @param request: Peticion HTTP
    @return: pagina de adminsitracion de proyectos
    """
    filtro = GroupFilter(request.GET, queryset=Group.objects.all())
    lista = GroupTable(filtro)
    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('admin_roles.html', {'lista': lista, 'filter': filtro},
                              context_instance=RequestContext(request))


@login_required
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
            return HttpResponseRedirect('/admin_roles')
        else:
            # hubo errores
            print form.errors
    else:
        # si no fue un post, mostrar el form
        form = RolForm()
    return render_to_response('add_rol.html', {'form': form}, context)


@login_required
def edit_rol(request, rol_name):
    """
    Renderiza la pagina de edicion de roles
    @param request: La peticion HTTP
    @param rol_name: El nombre del rol a editar
    @return: el form correspondiente
    """
    context = RequestContext(request)
    if request.method == 'GET':
        rol = Group.objects.get(name=rol_name)
        form = RolForm(instance=rol)
        return render_to_response('edit_rol.html', {'form': form, 'name': rol_name}, context)
    else:
        rol = Group.objects.get(name=rol_name)
        formulario = RolForm(request.POST, instance=rol)
        if formulario.eliminar:
            rol.delete()
            return HttpResponseRedirect('/admin_roles')
        lista_permisos = request.POST.getlist('permissions')
        nueva_lista = []
        for permiso_id in lista_permisos:
            permiso = Permission.objects.get(id=permiso_id)
            nueva_lista.append(permiso)
        rol.permissions = nueva_lista
        return HttpResponseRedirect('/admin_roles')


@login_required
def delete_rol(request, rol_name):
    """
    funcion para eliminar un rol
    @param request: Peticion HTTP
    @param rol_name: Nombre del rol a eliminar
    return: el form correspondiente
    """
    grupo = Group.objects.get(name=rol_name)
    if request.method == 'POST':
        grupo.delete()
        return HttpResponseRedirect('/admin_roles')


@login_required
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
            listidGroup = request.POST.getlist('groups')
            user = User.objects.get(id=idUser)
            grupos = []
            for idG in listidGroup:
                mygroup = Group.objects.get(id=idG)
                grupos.append(mygroup)
            user.groups = grupos
            if request.POST.__contains__('eliminar_roles'):
                user.groups = []
            return HttpResponseRedirect('/admin_roles')
        else:
            # hubo errores
            print form.errors
    else:
        # si no fue un post, mostrar el form
        form = asignarForm()
    return render_to_response('asignar_rol.html', {'form': form}, context)


@login_required
def admin_usuario(request):
    """
    Renderiza la pagina de administracion de usuario
    @param request: Peticion HTTP
    @return: el form correspondiente
    """
    #lista = User.objects.all()
    filtro = UserFilter(request.GET, queryset=User.objects.all())
    lista = UserTable(filtro)
    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('admin_usuarios.html', {'lista': lista, 'filter': filtro},
                              context_instance=RequestContext(request))


@login_required
def editar_usuario (request, username):
    """
    Renderiza la pagina de edicion de usuario/perfil de usuario
    @param request: Peticion HTTP
    @param username: Nombre de usuario a editar
    @return: el form correspondiente
    """
    context = RequestContext(request)
    if request.method == 'GET':
        usuario = User.objects.get(username=username)
        perfil_usuario = usuario.profile
        usuario_form = UserEditForm(instance=usuario, prefix="perfil_form")
        perfil_form = UserProfileEditForm(instance=perfil_usuario, prefix="usuario_form")
        return render_to_response('edit_usuario.html',
                                  {'usuario_form': usuario_form, 'perfil_form': perfil_form, 'name': usuario.username}
                                  , context)
    else:
        usuario = User.objects.get(username=username)
        perfil_usuario = usuario.profile
        usuario_form = UserEditForm(request.POST, instance=usuario, prefix="perfil_form")
        perfil_form = UserProfileEditForm(request.POST, instance=perfil_usuario, prefix="usuario_form")
        if usuario_form.is_valid() and perfil_form.is_valid():
            user1 = usuario_form.save()
            perfil_usuario.user = user1
            perfil_usuario.save()
            return HttpResponseRedirect('/admin_usuarios')
        else:
            print usuario_form.errors, perfil_form.errors
            return render_to_response('edit_usuario.html',
                                      {'usuario_form': usuario_form, 'perfil_form':perfil_form, 'name': usuario.username}
                                      , context)