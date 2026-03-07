from django.shortcuts import render
from .models import *
import json as simplejson
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Avg, Sum, F, Count, Q
from . import dataCountries as data

# Create your views here.
def get_compromisos(request):
	lista = []
	compromisos = Compromiso.objects.all()
	try:
		with open('compromisos/world.json', 'r') as file:
			data = simplejson.load(file)
			countries = data.get("features", [])
			lista_pais = compromisos.values_list('pais',flat=True)
			for x in countries:
				if x['id'] in lista_pais:
					lista.append(x)
	except FileNotFoundError:
		print(f"Error: The file was not found.")
	return HttpResponse(simplejson.dumps(list(lista)), content_type = 'application/json')

def get_compromisos_detalle(request):
	name = request.GET.get('name')
	lista = []
	country_display_to_value = dict((v, k) for k, v in data.COUNTRIES_CODE_CHOICES)
	display_name = name
	stored_value = country_display_to_value.get(display_name)

	comp = Compromiso.objects.get(pais = stored_value)
	lista.append((name,comp.total,comp.conteo_hombres,comp.conteo_mujeres))
	return HttpResponse(simplejson.dumps(list(lista)), content_type = 'application/json')
