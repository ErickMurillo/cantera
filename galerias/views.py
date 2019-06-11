from django.shortcuts import render,get_object_or_404
from .models import *
from evento.models import *
import datetime

# Create your views here.

def index_galeriasImagenes(request, template = 'list_galeria.html'):
	list_galeria = GaleriaImagenes.objects.order_by('titulo')

	dic_temas = {}
	for tema in Temas.objects.all():
		count = GaleriaImagenes.objects.filter(tematica = tema).count()
		if count != 0:
			dic_temas[tema] = count
	return render(request,template,locals())

def detalle_galeriaImagenes(request, slug, template = 'detail_galeria.html'):
	object = GaleriaImagenes.objects.get(slug = slug)

	dic_temas = {}
	for tema in Temas.objects.all():
		count = GaleriaImagenes.objects.filter(tematica = tema).count()
		if count != 0:
			dic_temas[tema] = count

	return render(request, template, locals())

def filtro_temas_img(request,tema,template="list_galeria.html"):
	return render(request,template,locals())


def index_galeriaVideos(request,template = 'list_galeria.html'):
	list_galeria = GaleriaVideos.objects.order_by('titulo')
	
	dic_temas = {}
	for tema in Temas.objects.all():
		count = GaleriaVideos.objects.filter(tematica = tema).count()
		if count != 0:
			dic_temas[tema] = count
	return render(request,template,locals())

def filtro_temas_vid(request,tema,template='list_galeria.html'):
	list_galeria = GaleriaVideos.objects.filter(tematica = tema).order_by('-id')

	dic_temas = {}
	for tema in Temas.objects.all():
		count = GaleriaVideos.objects.filter(tematica = tema).count()
		if count != 0:
			dic_temas[tema] = count

	return render(request,template,locals())
