from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from organizaciones.models import *
from actualidad.models import *
from evento.models import *
from configuracion.models import *
from foro.models import *
import datetime
from django.db.models import Count

def index(request,template='index.html'):
	# actualidad = Actualidad.objects.order_by('-created_on')[:6]
	actualidad = Actualidad.objects.filter(category__in = ['noticias','situacion-regional-genero']).order_by('created_on')
	hoy = datetime.date.today()
	eventos = Evento.objects.filter(inicio__gte = hoy).order_by('-inicio','-hora_inicio')[:3]
	foros = Foros.objects.annotate(conteo = Count('aportes')).order_by('-conteo','-aportes__fecha')[:3]
	alianzas = Contraparte.objects.order_by('nombre')

	return render(request, template,locals())

@login_required
def perfil(request,template='admin/org_index.html'):
	try:
		organizacion = Contraparte.objects.get(id = request.user.organizacion.id)
		return render(request, template,locals())
	except :
		return render(request, 'admin/error.html',locals())