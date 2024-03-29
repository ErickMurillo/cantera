from django.shortcuts import render,redirect
from .models import *
from evento.models import *
from organizaciones.models import Pais
import datetime
from taggit.models import *
from django.db.models import Q, Count

# Create your views here.
# def list_actualidad(request,template='list_actualidad.html'):
# 	if request.GET.get('buscador'):
# 		q = request.GET['buscador']
# 		list_object = Actualidad.objects.filter(
# 										Q(tittle__icontains = q) |
# 										Q(tematica__nombre__icontains = q) |
# 										Q(tags__name__icontains = q),
# 										category__in = ['noticias','situacion-regional-genero']).order_by('created_on')

# 	else:
# 		list_object = Actualidad.objects.filter(category__in = ['noticias','situacion-regional-genero']).order_by('created_on')

# 	list_paises = Pais.objects.order_by('nombre')
# 	hoy = datetime.date.today()
# 	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
# 	tags = Actualidad.tags.most_common( extra_filters={'id__in': list_object})[:6]

# 	return render(request, template, locals())

def filtro_pais(request,slug,category,template='list_actualidad.html'):
	hoy = datetime.date.today()
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(pais__icontains = q) |
										Q(tags__name__icontains = q),
										category = category,aprobado = True,
										created_on__lte = hoy).order_by('created_on')
	else:
		list_object = Actualidad.objects.filter(pais__slug = slug, category = category,aprobado = True,created_on__lte = hoy).order_by('created_on')

	list_paises = Actualidad.objects.filter(category = category,created_on__lte = hoy).values_list('pais__nombre','pais__slug').order_by('pais__nombre').distinct('pais__nombre')
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('inicio')[:3]
	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]
	pais = Pais.objects.get(slug = slug)

	return render(request, template, locals())

def filtro_categoria(request,category,template='list_actualidad.html'):
	hoy = datetime.date.today()
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category = category,aprobado = True,created_on__lte = hoy).order_by('-created_on')
		
	else:
		list_object = Actualidad.objects.filter(category = category,aprobado = True,created_on__lte = hoy).order_by('-created_on')

	list_paises = Actualidad.objects.filter(category = category,created_on__lte = hoy).values_list('pais__nombre','pais__slug').distinct('pais__nombre').order_by('pais__nombre')

	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('inicio')[:3]

	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request, template, locals())

def filtro_tag(request,slug,category,template='list_actualidad.html'):
	hoy = datetime.date.today()
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category = category,aprobado = True,created_on__lte = hoy).order_by('created_on')
		
	else:
		list_object = Actualidad.objects.filter(category = category,tags__slug = slug,aprobado = True,created_on__lte = hoy).order_by('created_on')

	list_paises = Actualidad.objects.filter(category = category,created_on__lte = hoy).values_list('pais__nombre','pais__slug').distinct('pais__nombre').order_by('pais__nombre')
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('inicio')[:3]
	ids = list_object.values_list('id',flat=True)
	tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

	return render(request, template, locals())

def detalle_actualidad(request,slug, template = 'detail_actualidad.html'):
	hoy = datetime.date.today()
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		object = Actualidad.objects.get(slug = slug)
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category = object.category,created_on__lte = hoy).order_by('created_on')
		return render(request,'list_actualidad.html',locals())

	else:
		object = Actualidad.objects.get(slug = slug)
		list_object = Actualidad.objects.filter(category = object.category,aprobado = True).order_by('created_on')
	
		list_paises = Actualidad.objects.filter(category = object.category).values_list('pais__nombre','pais__slug').distinct('pais__nombre').order_by('pais__nombre')
		prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
		ids = list_object.values_list('id',flat=True)
		tags = Actualidad.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:6]

		return render(request, template, locals())
