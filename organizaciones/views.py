from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from actualidad.models import *
from foro.models import *
from evento.models import *
from galerias.models import *
from actualidad.forms import *

# Create your views here.

#GENERAL VIEWS
def index_org(request, template = 'list_org.html'):
	list_object = Contraparte.objects.order_by('nombre')
	return render(request,template,locals())

def detalles_org(request, slug, template = 'detail_org.html'):
	detail_object = Contraparte.objects.get(slug = slug)
	return render(request, template, locals())

#-- ADMIN

def actualidad_list(request, template = 'admin/actualidad_index.html'):
	list_object = Actualidad.objects.filter(author = request.user.id)
	return render (request, template,locals())

@login_required
def actualidad_crear(request,template = 'admin/new_actualidad.html'):
	if request.method == 'POST':
		print('method post')
		form = ActualidadForms(request.POST, request.FILES)
		if form.is_valid():
			actualidad = form.save(commit=False)
			actualidad.author = request.user
			actualidad.save()
			form.save_m2m()
			return HttpResponseRedirect('/contrapartes/iniciativas-destacadas/eventos/')
	else:
		form = ActualidadForms()
	return render(request, template, locals())

@login_required
def actualidad_editar(request, slug, template = 'admin/edit_actualidad.html'):
	object = get_object_or_404(Actualidad, slug=slug)
	if request.method == 'POST':
		form = ActualidadForms(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.user = request.user
			form_uncommited.save()
			return HttpResponseRedirect('/contrapartes/actualidad/')
	else:
		form = ActualidadForms(instance=object)
	return render(request, template, locals())

def foros_list(request, template = 'admin/foros_list.html'):
	list_object_forum = Foros.objects.filter(usuario = request.user.id)
	return render(request,template,locals())

def foros_crear(request,template = 'admin/new_foro.html'):
	return render(request, template, locals())

def events_list(request,template = 'admin/events_list.html'):
	list_object_events = Evento.objects.filter(author = request.user.id)
	return render(request,template,locals())

def events_crear(request,template = 'admin/new_event.html'):
	return render(request, template, locals())

def galeria_list(request,template='admin/galeria_list.html'):
	list_objects_imagenes = GaleriaImagenes.objects.filter(usuario = request.user.id)
	list_objects_video = GaleriaVideos.objects.filter(usuario = request.user.id)
	return render(request,template,locals())

def galeria_img_crear(request,template = 'admin/new_galeria_img.html'):
	return render(request, template, locals())

def galeria_vid_crear(request,template = 'admin/new_galeria_vid.html'):
	return render(request, template, locals())