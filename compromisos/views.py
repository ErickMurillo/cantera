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
		list_fotos = []
		fotos = ''
		for foto in comp.fotoscompromisos_set.all()[:1]:
			fotos += '<div class="item-media"><img src='+str(foto.cached_img)+' alt=""></div>'

		html = '<div class="vertical-item content-padding big-padding with_border bottom_color_border tooltip_map" style="width: 250px;"><h5 class="">'+comp.get_pais_display()+'</h5><div class="">'+fotos+'</div><div class="item-content"><div class="value main_value" akhi="200">'+str(comp.total)+'</div><h5 class="">Compromisos</h5><ul class="sex_value"><li>Mujeres: <span class="value" akhi="200">'+str(comp.conteo_mujeres)+'</span></li><li>Hombres: <span class="value" akhi="200">'+str(comp.conteo_hombres)+'</span></li></ul></div></div>'

		dict['fotos'] = html

		lista.append(dict)

	return HttpResponse(simplejson.dumps(list(lista)), content_type = 'application/json')
