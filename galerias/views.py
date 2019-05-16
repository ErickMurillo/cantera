from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.

def index_galeriasImagenes(request, template = 'list_galeria.html'):
	list_galeria = GaleriaImagenes.objects.order_by('titulo')
	return render(request,template,locals())

def detalle_galeriaImagenes(request, slug, template = 'detail_galeria.html'):
	object = GaleriaImagenes.objects.get(slug = slug)


	return render(request, template, locals())
