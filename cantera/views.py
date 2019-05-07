from django.shortcuts import render

def index(request,template='index.html'):
	return render(request, template,locals())

def perfil(request,template='perfil.html'):
	return render(request, template,locals())