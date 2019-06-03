from django.shortcuts import render,redirect
from .models import *
from evento.models import *
import datetime
from taggit.models import *
from django.db.models import Q

# Create your views here.
def list_actualidad(request,template='list_actualidad.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category__in = [1,2,3]).order_by('created_on')

	else:
		list_object = Actualidad.objects.filter(category__in = [1,2,3]).order_by('created_on')

	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tags = Actualidad.tags.most_common( extra_filters={'id__in': list_object})[:6]

	return render(request, template, locals())

def filtro_categoria(request,category,template='list_actualidad.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category__in = [1,2,3]).order_by('created_on')
		
	else:
		list_object = Actualidad.objects.filter(category = category).order_by('created_on')

	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tags = Actualidad.tags.most_common( extra_filters={'id__in': list_object})[:6]

	return render(request, template, locals())

def filtro_tag(request,slug,template='list_actualidad.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_object = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										category__in = [1,2,3]).order_by('created_on')
		
	else:
		list_object = Actualidad.objects.filter(category__in = [1,2,3],tags__slug = slug).order_by('created_on')
	
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	tags = Actualidad.tags.most_common( extra_filters={'id__in': list_object})[:6]

	return render(request, template, locals())

def detalle_actualidad(request,slug, template = 'detail_actualidad.html'):
	object = Actualidad.objects.get(slug = slug)

	return render(request, template, locals())
