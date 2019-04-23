from django.shortcuts import render

# Create your views here.
def index(request,template='actualidad.html'):
	return render(request, template, locals())

def detail(request, template = 'actualidaDetalle.html'):
	return render(request, template, locals())
