from django.shortcuts import render
from .models import *
import json as simplejson
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Avg, Sum, F, Count, Q

# Create your views here.
def get_compromisos(request):
	lista = []
	compromisos = Compromiso.objects.all()
	for comp in compromisos:
		dict = {}
		dict['code3'] = comp.pais
		dict['value'] = comp.total
		dict['hombres'] = comp.conteo_hombres
		dict['mujeres'] = comp.conteo_mujeres
		lista.append(dict)

	return HttpResponse(simplejson.dumps(list(lista)), content_type = 'application/json')
