from django.shortcuts import render
from .models import *

# Create your views here.
def indexEventos(request,template='list_eventos.html'):
	event_list = Evento.objects.order_by('inicio')
	return render(request, template, locals())

def detailEventos(request,slug,template='detail_evento.html'):
	object = Evento.objects.get(slug = slug)
	return render(request, template,locals())