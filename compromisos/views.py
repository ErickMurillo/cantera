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
		html = ''
		for foto in comp.fotoscompromisos_set.all():
			html += '<div class="vertical-item content-padding big-padding bottom_color_border tooltip_map" style="width: 300px;"><h5 class="">Nicaragua</h5><div class="owl-carousel owl-theme owl-map"><div class="item-media"><a data-fancybox="gallery" href=""><img src="https://picsum.photos/300/224?random=1" alt=""></a></div><div class="item-media"><a data-fancybox="gallery" href=""><img src="https://picsum.photos/300/224?random=2" alt=""></a></div><div class="item-media"><a data-fancybox="gallery" href=""><img src="https://picsum.photos/300/224?random=3" alt=""></a></div><div class="item-media"><a data-fancybox="gallery" href=""><img src="https://picsum.photos/300/224?random=4" alt=""></a></div></div><div class="item-content"><div class="value main_value" akhi="200">0</div><h5 class="">Compromisos</h5><ul class="sex_value"><li>Mujeres: <span class="value" akhi="200">0</span></li><li>Hombres: <span class="value" akhi="200">0</span></li></ul></div></div>'
		dict['fotos'] = html

		lista.append(dict)

	return HttpResponse(simplejson.dumps(list(lista)), content_type = 'application/json')
