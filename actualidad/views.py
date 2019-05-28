from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def list_actualidad(request,template='list_actualidad.html'):
	list_object = Actualidad.objects.order_by('created_on')
	return render(request, template, locals())

def detalle_actualidad(request,slug, template = 'detail_actualidad.html'):
	object = Actualidad.objects.get(slug = slug)

	return render(request, template, locals())
