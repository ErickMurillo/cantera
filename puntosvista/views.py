from django.shortcuts import render
from .models import *

# Create your views here.

def list_puntos(request, template = 'list_puntos.html'):
	list_puntos_vista = Puntos.objects.order_by('tittle')
	return render(request,template,locals())

def point_details(request,slug,template='detail_puntos.html'):
	object = Puntos.objects.get(slug=slug)
	return render(request,template,locals())

