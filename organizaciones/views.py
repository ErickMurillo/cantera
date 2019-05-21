from django.shortcuts import render,redirect
from .models import *
from actualidad.models import *
from foro.models import *
from evento.models import *
from galerias.models import *

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

def foros_list(request, template = 'admin/foros_list.html'):
	list_object_forum = Foros.objects.filter(usuario = request.user.id)
	return render(request,template,locals())

def events_list(request,template = 'admin/events_list.html'):
	list_object_events = Evento.objects.filter(author = request.user.id)
	return render(request,template,locals())

def galeria_imagenes_list(request,template='admin/galeria_list.html'):
	list_objects_imagenes = GaleriaImagenes.objects.filter(usuario = request.user.id)
	list_objects_video = GaleriaVideos.objects.filter(usuario = request.user.id)
	return render(request,template,locals())