from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index_org(request, template = 'list_org.html'):
	list_object = Contraparte.objects.order_by('nombre')
	return render(request,template,locals())

def detalles_org(request, slug, template = 'detail_org.html'):
	object = Contraparte.objects.get(slug = slug)
	return render(request, template, locals())
