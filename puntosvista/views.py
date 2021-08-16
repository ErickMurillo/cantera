from django.shortcuts import render
from .models import *
import datetime
from evento.models import *
from django.db.models import Q
# Create your views here.

def list_puntos(request, template = 'list_puntos.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_puntos_vista = Puntos.objects.filter(
										Q(tittle__icontains = q) |
										Q(contenido__icontains = q),aprobado = True).order_by('tittle')
	else:
		list_puntos_vista = Puntos.objects.filter(aprobado = True).order_by('-id')
		hoy = datetime.date.today()
		prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]

	return render(request,template,locals())

def point_details(request,slug,template='detail_puntos.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_puntos_vista = Puntos.objects.filter(
										Q(tittle__icontains = q) |
										Q(contenido__icontains = q),aprobado = True).order_by('tittle')
		
		return render(request,'list_puntos.html',locals())
	else:
		object = Puntos.objects.get(slug=slug)
		hoy = datetime.date.today()
		prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
		return render(request,template,locals())

