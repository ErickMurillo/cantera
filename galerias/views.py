from django.shortcuts import render,get_object_or_404
from .models import *
from evento.models import *
import datetime

# Create your views here.

def index_galeriasImagenes(request, template = 'list_galeria.html'):
	list_galeria = GaleriaImagenes.objects.order_by('titulo')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	#tematica = GaleriaImagenes.tematica.most_common( extra_filters={'id__in': list_galeria})[:3]
	return render(request,template,locals())

def detalle_galeriaImagenes(request, slug, template = 'detail_galeria.html'):
	object = GaleriaImagenes.objects.get(slug = slug)


	return render(request, template, locals())
