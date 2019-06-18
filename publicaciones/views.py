from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from evento.models import *
import datetime
from taggit.models import *
from django.db.models import Q
# Create your views here.

def index_publicaciones(request,template='list_publicacion.html'):
	list_pub = Publicacion.objects.filter(tipo = 1).order_by('id')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]

	return render(request, template, locals())

def detail_publicacion(request,slug,template='detail_publicacion.html'):
	#object= Publicacion.objects.get(slug=slug)
	object = get_object_or_404(Publicacion, slug=slug)
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	
	return render(request,template, locals())

def index_guias(request,template='list_publicacion.html'):
	list_pub = Publicacion.objects.filter(tipo__in = [2]).order_by('id')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]

	return render(request,template,locals())

def detail_guias(request,slug,template='detail_publicacion.html'):
	object = Publicacion.objects.get(slug = slug)
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]

	return render(request,template,locals())
