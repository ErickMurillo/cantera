from django.shortcuts import render
from .models import *
import datetime
from evento.models import *
from django.db.models import Q
# Create your views here.

def list_puntos(request, template = 'list_puntos.html'):
	hoy = datetime.date.today()
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_puntos_vista = Puntos.objects.filter(
										Q(tittle__icontains = q) |
										Q(contenido__icontains = q),aprobado = True,fecha_creacion__lte = hoy).order_by('tittle')
	else:
		list_puntos_vista = Puntos.objects.filter(aprobado = True,fecha_creacion__lte = hoy).order_by('-id')
		prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]

	return render(request,template,locals())

def point_details(request,slug,template='detail_puntos.html'):
	hoy = datetime.date.today()
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_puntos_vista = Puntos.objects.filter(
										Q(tittle__icontains = q) |
										Q(contenido__icontains = q),aprobado = True,fecha_creacion__lte = hoy).order_by('tittle')
		
		return render(request,'list_puntos.html',locals())
	else:
		object = Puntos.objects.get(slug=slug)
		prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
		return render(request,template,locals())

