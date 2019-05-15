from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index_publicaciones(request,template='list_publicacion.html'):
	list_pub = Publicacion.objects.order_by('id')
	return render(request, template, locals())

def detail_publicacion(request,slug,template='detail_publicacion.html'):
	object= Publicacion.objects.get(slug=slug)

	return render(request,template, locals())