"""
Creado el 1 abril  2014
@author: Grupo 04
"""
from django import forms

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from proyecto.forms import ProyectoForm , ProyectoFilter, FaseForm
from principal.forms import UserForm, UserProfileForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User, Group
# Create your views here.
#from principal.models import Rol
from proyecto.models import Proyecto, Fase
from django.contrib.auth.decorators import login_required
from django_tables2   import RequestConfig
from proyecto.tables  import ProyectoTable , FasesTable
from django.views.generic.edit import UpdateView
from django.forms.util import ErrorList
# Create your views here.


@login_required
def admin_proyecto(request):
    """
    Renderiza la pagina de proyectos
    @param request: Peticion HTTP
    @return: el form correspondiente
    """
    #lista = Proyecto.objects.all()
    f = ProyectoFilter(request.GET, queryset=Proyecto.objects.all())
    lista = ProyectoTable(f)

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('admin_proyectos.html', {'lista': lista , 'filter': f}, context_instance=RequestContext(request))

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
            p = form.save(commit=False)
            p.usuario_modificacion = request.user
            p.save()
            return HttpResponseRedirect('/admin_proyectos')
        else:
            # hubo errores
            print form.errors
    else:
        # si no fue un post, mostrar el form
        form = ProyectoForm()
    return render_to_response('add_proyecto.html', {'form': form}, context)


@login_required
def proyecto_detail(request,id):
    """Metodo de para Editar un Proyecto en Particular

    """
    proyecto = Proyecto.objects.get(pk=int(id))

    if request.method == 'POST':
        form = ProyectoForm(request.POST,instance=proyecto)
    # el form es valido?
        if form.is_valid():
            # guardar
            estado = form.cleaned_data['estado']
            num_fases = form.cleaned_data['numero_fases']
            print "estado " + estado
            print "numero de fases  " + str(num_fases)
            print "proyecto numero de fases viejo" + str(  Proyecto.objects.get(pk=int(id)).numero_fases)
            if Proyecto.objects.get(pk=int(id)).numero_fases != num_fases:
                print "cambio numero de fases"
                if proyecto.estado != "Pendiente":
                    error = "No se puede editar las fases de un Proyecto en estado distinto a Pendiente"

                    errors = form._errors.setdefault("numero_fases", ErrorList())
                    errors.append(error)
                    return render_to_response('edit_proyecto1.html', {'form': form ,'id':proyecto.id}, context_instance=RequestContext(request))


            f=form.save(commit=False)
            f.usuario_modificacion = request.user
            f.save()
            return HttpResponseRedirect('/admin_proyectos')
        else:
            # hubo errores
            print form.errors
    else:
        form = ProyectoForm(instance=proyecto)
        return render_to_response('edit_proyecto1.html', {'form': form ,'id':proyecto.id}, context_instance=RequestContext(request))


@login_required
class ProyectoUpdate(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'edit_proyecto.html'
    success_url = '/admin_proyectos/'


@login_required
def delete_proyecto(request,id):
    """
    funcion para eliminar un proyecto
    """
    server = get_object_or_404(Proyecto, pk=id)
    if request.method=='POST':
        server.delete()
        return HttpResponseRedirect('/admin_proyectos')


@login_required
def proyecto_view(request,id_proyecto):
    """

    Lista las fases de un proyecto

    """

    fases = Fase.objects.filter(proyecto= id_proyecto)
    lista = FasesTable(fases)

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('proyecto_view.html', {'lista': lista }, context_instance=RequestContext(request))


@login_required
def fase_detail(request,id):
    """Metodo de para Editar una Fase en Particular

    """
    fase = Fase.objects.get(pk=int(id))
    proyecto = fase.proyecto

    if request.method == 'POST':
        form = FaseForm(request.POST,instance=fase)
    # el form es valido?
        if form.is_valid():
            # guardar
            f = form.save(commit=False)
            f.usuario_modificacion = request.user
            f.save()
            return HttpResponseRedirect('/proyecto_view/'+ str(proyecto.id)+"/")
        else:
            # hubo errores
            print form.errors
    else:
        form = FaseForm(instance=fase)
        return render_to_response('edit_fase.html', {'form': form ,'id':fase.id}, context_instance=RequestContext(request))


@login_required
def delete_fase(request,id):
    """
    funcion para eliminar una Fase
    """
    fase = get_object_or_404(Fase, pk=id)
    proyecto = fase.proyecto
    proyecto.numero_fases= proyecto.numero_fases -1
    proyecto.save()

    if request.method=='POST':
        #Controlar si el Proyecto esta activo
        fase.delete()
        return HttpResponseRedirect('/proyecto_view/'+ str(proyecto.id)+"/")














