from django.shortcuts import render,get_object_or_404
from django.db.models import Count,Sum
from .models import *
from evento.models import *
import datetime
import collections

# Create your views here.
def index_galeriasImagenes(request, template = 'list_galeria.html'):
	list_galeria = GaleriaImagenes.objects.order_by('-id')
	list_tematica = collections.OrderedDict()
	for x in Temas.objects.all():
		galeria = GaleriaImagenes.objects.filter(tematica = x).count()
		if galeria:
			list_tematica[x] = galeria

	return render(request,template,locals())

def detalle_galeriaImagenes(request, slug, template = 'detail_galeria.html'):
	object = GaleriaImagenes.objects.get(slug = slug)
	related_gal = GaleriaImagenes.objects.filter(tematica = object.tematica.id).exclude(id=object.id).order_by('-id')[:3]
	latest_gal = GaleriaImagenes.objects.exclude(id=object.id).order_by('-id')[:3]
	return render(request, template, locals())

def filtro_temas_img(request,tema,template="list_galeria.html"):
	list_galeria = GaleriaImagenes.objects.filter(tematica = tema).order_by('-id')
	list_tematica = collections.OrderedDict()
	for x in Temas.objects.exclude(id = tema):
		galeria = GaleriaImagenes.objects.filter(tematica = x).count()
		if galeria:
			list_tematica[x] = galeria

	return render(request,template,locals())


def index_galeriaVideos(request,template = 'list_galeria.html'):
	list_galeria = GaleriaVideos.objects.order_by('-id')
	list_tematica = collections.OrderedDict()
	for x in Temas.objects.all():
		galeria = GaleriaVideos.objects.filter(tematica = x).count()
		if galeria:
			list_tematica[x] = galeria

	return render(request,template,locals())

def detalle_galeria_vid(request,slug,template ='detail_galeria_vid.html'):
	object = GaleriaVideos.objects.get(slug = slug)
	return render(request,template,locals())

def filtro_temas_vid(request,tema,template='list_galeria.html'):
	list_galeria = GaleriaVideos.objects.filter(tematica = tema).order_by('-id')
	list_tematica = collections.OrderedDict()
	for x in Temas.objects.exclude(id = tema):
		galeria = GaleriaVideos.objects.filter(tematica = x).count()
		if galeria:
			list_tematica[x] = galeria

	return render(request,template,locals())
