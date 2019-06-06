from django.shortcuts import render
from .models import *
import datetime
from evento.models import *
# Create your views here.

def list_puntos(request, template = 'list_puntos.html'):
	list_puntos_vista = Puntos.objects.order_by('tittle')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	return render(request,template,locals())

def point_details(request,slug,template='detail_puntos.html'):
	object = Puntos.objects.get(slug=slug)
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	return render(request,template,locals())

