from django.shortcuts import render,redirect
from .models import *
# from actualidad.models import *
# from actualidad.forms import *

# Create your views here.
def index_org(request, template = 'list_org.html'):
	list_object = Contraparte.objects.order_by('nombre')
	return render(request,template,locals())

def detalles_org(request, slug, template = 'detail_org.html'):
	detail_object = Contraparte.objects.get(slug = slug)
	return render(request, template, locals())

def actualidad_list(request, template = 'admin/actualidad_index.html'):
	#list_object = Actualidad.objects.filter(user_id = request.author.id)
	return render (request, template,locals())

def foros_list(request, template = 'admin/foros_list.html'):
	return render(request,template,locals())

def iniciativas_list(request,template = 'admin/iniciativas_list.html'):
	return render(request,template),locals()

def recursos_metod_list(request,template='admin/recursos_metod_list.html'):
	return render(request,template,locals())