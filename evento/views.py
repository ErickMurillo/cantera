from django.shortcuts import render
from .models import *
from actualidad.models import *
import datetime
from taggit.models import *
from django.db.models import Q


# Create your views here.
def indexEventos(request,template='list_eventos.html'):
	event_list = Evento.objects.order_by('inicio')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tags = Evento.tags.most_common()[:6]
	return render(request, template, locals())

def detailEventos(request,slug,template='detail_evento.html'):
	object = Evento.objects.get(slug = slug)
	event_list = Evento.objects.order_by('inicio')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tagsevent = Evento.tags.most_common()[:6]
	print(tagsevent)
	return render(request, template,locals())

def indexCampanias(request,template='list_campanias.html'):
	list_object = Actualidad.objects.filter(category__in = ['campanas']).order_by('created_on')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tags = Actualidad.tags.most_common( extra_filters={'id__in': list_object})[:6]
	return render(request,template,locals())

def detailCampanias(request,slug,template='detail_campanas.html'):
	object = Actualidad.objects.get(slug = slug)
	list_object = Actualidad.objects.filter(category__in = ['campanas']).order_by('created_on')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tags = Actualidad.tags.most_common( extra_filters={'id__in': list_object})[:6]
	return render(request,template,locals())

def indexConcursos(request, template="list_concursos.html"):
	list_object = Actualidad.objects.filter(category__in = ['concursos']).order_by('created_on')

	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tags = Actualidad.tags.most_common( extra_filters={'id__in': list_object})[:6]
	return render(request,template,locals())

def detailConcursos(request,slug,template='detail_concursos.html'):
	object = Actualidad.objects.get(slug = slug)
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	return render(request,template,locals())

def filtro_tag_concurso(request,slug,template='list_concursos.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category__in = ['concursos']).order_by('created_on')
		
	else:
		list_object = Actualidad.objects.filter(category__in = ['concursos'],tags__slug = slug).order_by('created_on')
	
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tags = Actualidad.tags.most_common( extra_filters={'id__in': list_object})[:6]

	return render(request, template, locals())

def filtro_tag_campanias(request,slug,template='list_campanias.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category__in = ['campanas']).order_by('created_on')
		
	else:
		list_object = Actualidad.objects.filter(category__in = ['campanas'],tags__slug = slug).order_by('created_on')
	
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tags = Actualidad.tags.most_common( extra_filters={'id__in': list_object})[:6]

	return render(request, template, locals())

def filtro_tag_eventos(request,slug,template='list_eventos.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		event_list = Evento.objects.filter(
										Q(tittle__icontains = q) |
										Q(tags__name__icontains = q)).order_by('inicio')
		
	else:
		event_list = Evento.objects.filter(tags__slug = slug).order_by('inicio')
	
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tags = Evento.tags.most_common()[:6]

	return render(request, template, locals())