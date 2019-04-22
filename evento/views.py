from django.shortcuts import render

# Create your views here.
def index(request,template='Eventos.html'):
	return render(request, template, locals())