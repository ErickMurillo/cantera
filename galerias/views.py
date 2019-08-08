from django.shortcuts import render,get_object_or_404
from django.db.models import Count,Sum
from .models import *
from evento.models import *
import datetime
import collections
from django.db.models import Q

# Create your views here.
def index_galeriasImagenes(request, template = 'list_galeria.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_galeria = GaleriaImagenes.objects.filter(
												Q(titulo__icontains = q) |
												Q(tematica__nombre__icontains = q)).order_by('-id')

	else:
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
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_galeria = GaleriaVideos.objects.filter(
												Q(titulo__icontains = q) |
												Q(tematica__nombre__icontains = q),aprobado = True).order_by('-id')

	else:
		list_galeria = GaleriaVideos.objects.filter(aprobado = True).order_by('-id')
		
	list_tematica = collections.OrderedDict()
	for x in Temas.objects.all():
		galeria = GaleriaVideos.objects.filter(tematica = x,aprobado = True).count()
		if galeria:
			list_tematica[x] = galeria

	return render(request,template,locals())

def detalle_galeria_vid(request,slug,template ='detail_galeria_vid.html'):
	object = GaleriaVideos.objects.get(slug = slug)
	list_tematica = collections.OrderedDict()
	for x in Temas.objects.all():
		galeria = GaleriaVideos.objects.filter(tematica = x,aprobado = True).count()
		if galeria:
			list_tematica[x] = galeria
	return render(request,template,locals())

def filtro_temas_vid(request,tema,template='list_galeria.html'):
	list_galeria = GaleriaVideos.objects.filter(tematica = tema,aprobado = True).order_by('-id')
	list_tematica = collections.OrderedDict()
	for x in Temas.objects.exclude(id = tema):
		galeria = GaleriaVideos.objects.filter(tematica = x,aprobado = True).count()
		if galeria:
			list_tematica[x] = galeria

	return render(request,template,locals())


def index_galeriaaudio(request,template = 'list_galeria.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		list_galeria = Audios.objects.filter(
												Q(titulo__icontains = q) |
												Q(tematica__nombre__icontains = q),aprobado = True).order_by('-id')

	else:
		list_galeria = Audios.objects.filter(aprobado = True).order_by('-id')
		
	list_tematica = collections.OrderedDict()
	for x in Temas.objects.all():
		galeria = Audios.objects.filter(tematica = x,aprobado = True).count()
		if galeria:
			list_tematica[x] = galeria

	return render(request,template,locals())

def detalle_galeria_audio(request,slug,template ='detail_galeria_vid.html'):
	object = Audios.objects.get(slug = slug)
	list_tematica = collections.OrderedDict()
	for x in Temas.objects.all():
		galeria = Audios.objects.filter(tematica = x,aprobado = True).count()
		if galeria:
			list_tematica[x] = galeria

	return render(request,template,locals())

def filtro_temas_audio(request,tema,template='list_galeria.html'):
	list_galeria = Audios.objects.filter(tematica = tema).order_by('-id')
	list_tematica = collections.OrderedDict()
	for x in Temas.objects.exclude(id = tema):
		galeria = Audios.objects.filter(tematica = x).count()
		if galeria:
			list_tematica[x] = galeria

	return render(request,template,locals())