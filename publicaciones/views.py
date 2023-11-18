from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from evento.models import *
import datetime
from taggit.models import *
from django.db.models import Q, Count
# Create your views here.

def index_publicaciones(request,template='list_publicacion.html'):
	list_pub = Publicacion.objects.filter(tipo = 1,aprobado = True).order_by('-id')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
	ids = list_pub.values_list('id',flat=True)
	tags = Publicacion.tags.most_common(min_count=2,extra_filters={'id__in': ids})[:118]
	return render(request, template, locals())

def detail_publicacion(request,slug,template='detail_publicacion.html'):
	#object= Publicacion.objects.get(slug=slug)
	object = get_object_or_404(Publicacion, slug=slug)
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
	
	return render(request,template, locals())

def index_guias(request,template='list_publicacion.html'):
	list_pub = Publicacion.objects.filter(tipo__in = [2],aprobado = True).order_by('-id')
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]

	return render(request,template,locals())

def detail_guias(request,slug,template='detail_publicacion.html'):
	object = Publicacion.objects.get(slug = slug)
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]

	return render(request,template,locals())

def filtro_tags(request,template='list_publicacion.html',tag=None):
	list_pub = Publicacion.objects.filter(tipo = 1,aprobado = True,tags__slug = tag).order_by('-id')
	tags_filter = Publicacion.objects.exclude(tags__slug = tag).annotate(num_times=Count('tags', distinct=True)).order_by('-num_times').values_list('tags__name','tags__slug')[:24]
	hoy = datetime.date.today()
	prox_eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio')[:3]
	return render(request,template,locals())


from haystack.query import SearchQuerySet
from haystack.views import SearchView, search_view_factory
from haystack.forms import ModelSearchForm

def search_publicacion(request):
	sqs = SearchQuerySet().models(Publicacion).order_by('-id')
	view = search_view_factory(
		view_class=SearchView,
		template='search/search_publicacion.html',
		searchqueryset=sqs,
		form_class=ModelSearchForm,
		results_per_page=10
		)
	return view(request)
