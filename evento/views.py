from django.shortcuts import render
from .models import *
from actualidad.models import *
import datetime
from taggit.models import *
from django.db.models import Q
from organizaciones.models import Pais


# Create your views here.
def indexEventos(request,template='list_eventos.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		event_list = Evento.objects.filter(
										Q(tittle__icontains = q) |
										Q(tags__name__icontains = q) |
										Q(descripcion__icontains = q),aprobado = True).order_by('-inicio').distinct()
	else:
		event_list = Evento.objects.filter(aprobado = True).order_by('-inicio')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
	tags = Evento.tags.most_common()[:6]

	return render(request, template, locals())

def detailEventos(request,slug,template='detail_evento.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		event_list = Evento.objects.filter(
										Q(tittle__icontains = q) |
										Q(tags__name__icontains = q) |
										Q(descripcion__icontains = q),aprobado = True).order_by('-inicio').distinct()
		return render(request, 'list_eventos.html', locals())
	else:
		object = Evento.objects.get(slug = slug)
		event_list = Evento.objects.filter(aprobado = True).order_by('inicio')
		hoy = datetime.date.today()
		prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
		tagsevent = Evento.tags.most_common()[:6]
		return render(request, template,locals())

def indexCampanias(request,template='list_campanias.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category__in = ['campanas'],aprobado = True).order_by('-created_on')
	else:
		list_object = Actualidad.objects.filter(category__in = ['campanas'],aprobado = True).order_by('-created_on')

	list_paises = Actualidad.objects.filter(category = 'campanas').values_list('pais__nombre','pais__slug').order_by('pais__nombre').distinct('pais__nombre')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('inicio')[:3]
	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]
	return render(request,template,locals())

def detailCampanias(request,slug,template='detail_campanas.html'):
	object = Actualidad.objects.get(slug = slug)
	list_object = Actualidad.objects.filter(category__in = ['campanas'],aprobado = True).order_by('-created_on')
	
	list_paises = Actualidad.objects.filter(category = 'campanas').values_list('pais__nombre','pais__slug').order_by('pais__nombre').distinct('pais__nombre')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('inicio')[:3]
	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]
	return render(request,template,locals())

def indexConcursos(request, template="list_concursos.html"):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category__in = ['concursos'],aprobado = True).order_by('-created_on')
	else:
		list_object = Actualidad.objects.filter(category__in = ['concursos'],aprobado = True).order_by('-created_on')

	list_paises = Actualidad.objects.filter(category = 'concursos').values_list('pais__nombre','pais__slug').order_by('pais__nombre').distinct('pais__nombre')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('inicio')[:3]
	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]
	return render(request,template,locals())

def detailConcursos(request,slug,template='detail_concursos.html'):
	object = Actualidad.objects.get(slug = slug)
	list_paises = Actualidad.objects.filter(category = 'concursos').values_list('pais__nombre','pais__slug').order_by('pais__nombre').distinct('pais__nombre')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
	list_object = Actualidad.objects.filter(category__in = ['concursos'],aprobado = True).order_by('-created_on')
	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]
	return render(request,template,locals())

def filtro_tag_concurso(request,slug,template='list_concursos.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category__in = ['concursos'],aprobado = True).order_by('-created_on')
		
	else:
		list_object = Actualidad.objects.filter(category__in = ['concursos'],tags__slug = slug,aprobado = True).order_by('-created_on')
	list_paises = Actualidad.objects.filter(category = 'concursos').values_list('pais__nombre','pais__slug').order_by('pais__nombre').distinct('pais__nombre')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request, template, locals())

def filtro_pais_conc(request,slug,template='list_campanias.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(pais__icontains = q),
										category__in = ['concursos'],aprobado = True).order_by('-created_on')
	else:
		list_object = Actualidad.objects.filter(pais__slug = slug, category__in = ['concursos'],aprobado = True).order_by('-created_on')
		
	list_paises = Actualidad.objects.filter(category = 'concursos').values_list('pais__nombre','pais__slug').order_by('pais__nombre').distinct('pais__nombre')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]
	return render(request,template,locals())

def filtro_pais_camp(request,slug,template='list_campanias.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(pais__icontains = q),
										category__in = ['campanas'],aprobado = True).order_by('-created_on')
	else:
		list_object = Actualidad.objects.filter(pais__slug = slug, category__in = ['campanas'],aprobado = True).order_by('created_on')

	list_paises = Actualidad.objects.filter(category = 'campanas').values_list('pais__nombre','pais__slug').order_by('pais__nombre').distinct('pais__nombre')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]
	return render(request,template,locals())

def filtro_tag_campanias(request,slug,template='list_campanias.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category__in = ['campanas'],aprobado = True).order_by('-created_on')
		
	else:
		list_object = Actualidad.objects.filter(category__in = ['campanas'],tags__slug = slug,aprobado = True).order_by('created_on')
	list_paises = Actualidad.objects.filter(category = 'campanas').values_list('pais__nombre','pais__slug').order_by('pais__nombre').distinct('pais__nombre')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request, template, locals())

def filtro_tag_eventos(request,slug,template='list_eventos.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		event_list = Evento.objects.filter(
										Q(tittle__icontains = q) |
										Q(tags__name__icontains = q),aprobado = True).order_by('-inicio').distinct()
		
	else:
		event_list = Evento.objects.filter(tags__slug = slug,aprobado = True).order_by('-inicio')
	
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
	tags = Evento.tags.most_common()[:6]

	return render(request, template, locals())