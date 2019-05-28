from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import *
from actualidad.models import *
from foro.models import *
from evento.models import *
from galerias.models import *
from puntosvista.models import *
from actualidad.forms import *
from evento.forms import *
from galerias.forms import *
from puntosvista.forms import *
from .forms import *

# Create your views here.

#GENERAL VIEWS
def index_org(request, template = 'list_org.html'):
	list_object = Contraparte.objects.order_by('nombre')
	return render(request,template,locals())

def detalles_org(request, slug, template = 'detail_org.html'):
	detail_object = Contraparte.objects.get(slug = slug)
	return render(request, template, locals())

#-- ADMIN
@login_required
def org_editar(request,id, template = 'admin/org_edit.html'):
	#obtener la organizacion asociada al usuario
	usr_org = Contraparte.objects.get(id = request.user.organizacion.id)
	# Validar que la organizacion que se desea editar es la asignada al usuario
	if str(usr_org.id) == id:
		contra = get_object_or_404(Contraparte, id=id)
		FormSetInit = inlineformset_factory(Contraparte, Redes, form=RedesFrom,extra=11,max_num=11)

		if request.method == 'POST':
			form = ContraparteForms(data=request.POST,instance=contra,files=request.FILES)
			formset = FormSetInit(request.POST,request.FILES,instance=contra)

			if form.is_valid() and formset.is_valid():
				form_uncommited = form.save(commit=False)
				form_uncommited.user = request.user
				form_uncommited.save()

				formset.save()
				return HttpResponseRedirect('/accounts/profile/')
		else:
			form = ContraparteForms(instance=contra)
			formset = FormSetInit(instance=contra)
		return render(request, template, locals())
	else:
		return HttpResponse('Bad request')

def actualidad_list(request, template = 'admin/actualidad_index.html'):
	list_object = Actualidad.objects.filter(author = request.user.id)
	return render (request, template,locals())

@login_required
def actualidad_crear(request,template = 'admin/new_actualidad.html'):
	if request.method == 'POST':
		form = ActualidadForms(request.POST, request.FILES)

		if form.is_valid():
			actualidad = form.save(commit=False)
			actualidad.author = request.user
			actualidad.save()
			form.save_m2m()
			return HttpResponseRedirect('/alianzas/actualidad/')
	else:
		form = ActualidadForms()

	return render(request, template, locals())

@login_required
def actualidad_editar(request, id, template = 'admin/edit_actualidad.html'):
	object = get_object_or_404(Actualidad, id=id)
	if request.method == 'POST':
		form = ActualidadForms(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.author = request.user
			form_uncommited.save()
			return HttpResponseRedirect('/alianzas/actualidad/')
	else:
		form = ActualidadForms(instance=object)
	return render(request, template, locals())

@login_required
def eliminar_actualidad(request, id):
	actualidad = Actualidad.objects.get(id = id).delete()
	return HttpResponseRedirect('/alianzas/actualidad/')


def foros_list(request, template = 'admin/foros_list.html'):
	list_object_forum = Foros.objects.filter(usuario = request.user.id)
	return render(request,template,locals())

@login_required
def foros_crear(request,template = 'admin/new_foro.html'):
	return render(request, template, locals())

def events_list(request,template = 'admin/events_list.html'):
	list_object_events = Evento.objects.filter(author = request.user.id)
	return render(request,template,locals())

def edit_event(request, template = 'edit_event.html'):
	return render(request,template,locals())

@login_required
def events_crear(request,template = 'admin/new_event.html'):
	if request.method == 'POST':
		form = EventsForms(request.POST, request.FILES)
		if form.is_valid():
			event = form.save(commit=False)
			event.author = request.user
			event.save()
			form.save_m2m()
			return HttpResponseRedirect('/alianzas/iniciativas-destacadas/eventos/')
	else:
		form = EventsForms()
	return render(request, template, locals())

@login_required
def events_editar(request, id, template = 'admin/new_event.html'):
	object = get_object_or_404(Evento, id=id)
	if request.method == 'POST':
		form = EventsForms(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.author = request.user
			form_uncommited.save()
			return HttpResponseRedirect('/alianzas/iniciativas-destacadas/eventos/')
	else:
		form = EventsForms(instance=object)

	return render(request, template, locals())

@login_required
def events_eliminar(request, id):
	nota = Evento.objects.get(id = id).delete()
	return HttpResponseRedirect('/alianzas/iniciativas-destacadas/eventos/')

@login_required
def galeria_list(request,template='admin/galeria_list.html'):
	list_objects_imagenes = GaleriaImagenes.objects.filter(usuario = request.user.id)
	list_objects_video = GaleriaVideos.objects.filter(usuario = request.user.id)
	return render(request,template,locals())

@login_required
def galeria_img_crear(request,template = 'admin/new_galeria_img.html'):
	FormSetInit = inlineformset_factory(GaleriaImagenes, Imagenes, form=ImagenesForm,extra=12,max_num=12)
	if request.method == 'POST':
		form = GaleriaImagenesForm(request.POST, request.FILES)
		formset = FormSetInit(request.POST,request.FILES)
		if form.is_valid() and formset.is_valid():
			galeria = form.save(commit=False)
			galeria.usuario = request.user
			galeria.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.imagenes = galeria
				instance.save()
			formset.save_m2m()

			return HttpResponseRedirect('/alianzas/recursos-metodologicos/galerias/')
	else:
		form = GaleriaImagenesForm()
		formset = FormSetInit()
	return render(request, template, locals())

@login_required
def galeria_img_editar(request, id, template = 'admin/new_galeria_img.html'):
	object = get_object_or_404(GaleriaImagenes, id=id)
	FormSetInit = inlineformset_factory(GaleriaImagenes, Imagenes, form=ImagenesForm,extra=12,max_num=12)
	if request.method == 'POST':
		form = GaleriaImagenesForm(data=request.POST,instance=object,files=request.FILES)
		formset = FormSetInit(request.POST,request.FILES,instance=object)

		if form.is_valid() and formset.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.save()

			formset.save()
			return HttpResponseRedirect('/alianzas/recursos-metodologicos/galerias/')
	else:
		form = GaleriaImagenesForm(instance=object)
		formset = FormSetInit(instance=object)
	return render(request, template, locals())

@login_required
def galeria_img_eliminar(request,id):
	galeria_img = GaleriaImagenes.objects.get(id=id).delete()
	return HttpResponseRedirect('/alianzas/recursos-metodologicos/galerias/')

@login_required
def galeria_vid_crear(request,template = 'admin/new_galeria_vid.html'):
	if request.method == 'POST':
		form = GaleriaVideosForm(request.POST, request.FILES)
		if form.is_valid():
			publi = form.save(commit=False)
			publi.usuario = request.user
			publi.save()

			return HttpResponseRedirect('/alianzas/recursos-metodologicos/galerias/')
	else:
		form = GaleriaVideosForm()
	return render(request, template, locals())

@login_required
def galeria_vid_editar(request, id, template = 'admin/new_galeria_vid.html'):
	object = get_object_or_404(GaleriaVideos, id=id)
	if request.method == 'POST':
		form = GaleriaVideosForm(request.POST, request.FILES, instance=object)
		if form.is_valid():
			video = form.save(commit=False)
			video.save()
			return HttpResponseRedirect('/alianzas/recursos-metodologicos/galerias/')
	else:
		form = GaleriaVideosForm(instance=object)
	return render(request,template,locals())

@login_required
def galeria_vid_eliminar(request,id):
	galeria_vid = GaleriaVideos.objects.get(id=id).delete()
	return HttpResponseRedirect('/alianzas/recursos-metodologicos/galerias/')

#Puntos de vista
@login_required
def puntos_vista_list(request,template = 'admin/puntos_list.html'):
	list_object_puntos = Puntos.objects.filter(usuario = request.user.id)
	return render(request,template,locals())

@login_required
def puntos_vista_crear(request,template = 'admin/new_punto.html'):
	if request.method == 'POST':
		form = PuntosForms(request.POST, request.FILES)
		if form.is_valid():
			punto = form.save(commit=False)
			punto.usuario = request.user
			punto.save()
			return HttpResponseRedirect('/alianzas/puntos-vista/')
	else:
		form = PuntosForms()
	return render(request, template, locals())

@login_required
def puntos_vista_edit(request,slug,template = 'admin/edit_puntos.html'):
	object = get_object_or_404(Puntos, slug=slug)
	if request.method == 'POST':
		form = PuntosForms(request.POST, request.FILES, instance = object)
		if form.is_valid():
			puntos = form.save()
			puntos.usuario = request.user
			puntos.save()
			return HttpResponseRedirect('/alianzas/puntos-vista/')
	else:
		form = PuntosForms(instance = object)
	return render(request,template,locals())

@login_required
def puntos_vista_eliminar(request,id):
	puntos_vista = Puntos.objects.get(id = id).delete()
	return HttpResponseRedirect('/alianzas/puntos-vista/')
