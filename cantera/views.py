from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from organizaciones.models import *

def index(request,template='index.html'):
	return render(request, template,locals())

@login_required
def perfil(request,template='admin/org_index.html'):
	try:
		organizacion = Contraparte.objects.get(id = request.user.organizacion.id)
		return render(request, template,locals())
	except :
		return HttpResponse('Bad request')