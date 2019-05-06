from django.shortcuts import render

def perfil(request,template='eventDetails.html'):
	return render(request, template,locals())