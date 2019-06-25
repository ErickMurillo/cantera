from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from organizaciones.models import *
from actualidad.models import *
from evento.models import *
from configuracion.models import *
from foro.models import *
import datetime
from django.db.models import Count
from users.models import *
from users.forms import *

def index(request,template='index.html'):
	# actualidad = Actualidad.objects.order_by('-created_on')[:6]
	actualidad = Actualidad.objects.filter(category__in = ['noticias','situacion-regional-genero']).order_by('created_on')
	hoy = datetime.date.today()
	eventos = Evento.objects.filter(inicio__gte = hoy).order_by('-inicio','-hora_inicio')[:3]
	foros = Foros.objects.annotate(conteo = Count('aportes')).order_by('-conteo','-aportes__fecha')[:3]
	alianzas = Contraparte.objects.order_by('nombre')
	slider = Slider.objects.all()

	return render(request, template,locals())

@login_required
def perfil(request,template='admin/org_index.html'):
	try:
		organizacion = Contraparte.objects.get(id = request.user.organizacion.id)
		return render(request, template,locals())
	except :
		return render(request, 'admin/error.html',locals())

def contacto(request,template='contact.html'):
	return render(request,template,locals())

@login_required
def editar_perfil(request,id,template='admin/editar_perfil.html'):
	user = User.objects.get(id = id)

	if request.method == 'POST':
		redirect_to = request.POST.get('next', '')
		form = UserChangeForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.save()

			return HttpResponseRedirect(redirect_to)
			
	else:
		form = UserChangeForm(instance=user)

	return render(request,template,locals())