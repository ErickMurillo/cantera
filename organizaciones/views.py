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
from foro.forms import *
from .forms import *
from users.models import *
from publicaciones.models import *
from publicaciones.forms import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

#GENERAL VIEWS
def index_org(request, template = 'list_org.html'):
	list_object = Contraparte.objects.exclude(nombre = 'Particular').order_by('nombre')
	return render(request,template,locals())

def detalles_org(request, slug, template = 'detail_org.html'):
	detail_object = Contraparte.objects.get(slug = slug)
	return render(request, template, locals())

#-- ADMIN
@login_required
def org_editar(request,id, template = 'admin/org_edit.html'):
	contra = get_object_or_404(Contraparte, id=id)
	FormSetInit = inlineformset_factory(Contraparte, Redes, form=RedesFrom,extra=1)

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

def actualidad_list(request, template = 'admin/actualidad_list.html'):
	list_object = Actualidad.objects.filter(author = request.user.id,category__in = ['noticias','situacion-regional-genero'])
	return render (request, template,locals())

@login_required
def actualidad_crear(request,template = 'admin/actualidad.html'):
	FormSetInit = inlineformset_factory(Actualidad,Galeria,form=GaleriaForm,extra=1)
	if request.method == 'POST':
		form = ActualidadForms(request.POST, request.FILES)
		formset = FormSetInit(request.POST, request.FILES)
		if form.is_valid() and formset.is_valid():
			actualidad = form.save(commit=False)
			actualidad.author = request.user
			actualidad.category = 'noticias'
			actualidad.aprobado = False
			actualidad.save()
			form.save_m2m()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.actualidad = actualidad
				instance.save()
			formset.save_m2m()
			
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/correo.txt', {'obj': actualidad,})

				html_content = render_to_string('email/correo.txt', {'obj': actualidad,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return redirect('/alianzas/actualidad/'+'?new=new_act')
			except:
				pass
	else:
		form = ActualidadForms()
		formset = FormSetInit()

	return render(request, template, locals())

@login_required
def actualidad_editar(request, id, template = 'admin/actualidad.html'):
	object = get_object_or_404(Actualidad, id=id)
	FormSetInit = inlineformset_factory(Actualidad,Galeria,form=GaleriaForm,extra=1)
	if request.method == 'POST':
		form = ActualidadForms(request.POST, request.FILES, instance=object)
		formset = FormSetInit(request.POST, request.FILES, instance=object)
		if form.is_valid() and formset.is_valid():
			form_uncommited = form.save()
			form_uncommited.author = request.user
			form_uncommited.save()

			formset.save()
			return HttpResponseRedirect('/alianzas/actualidad/')
	else:
		form = ActualidadForms(instance=object)
		formset = FormSetInit(instance=object)

	return render(request, template, locals())

@login_required
def eliminar_actualidad(request, id):
	actualidad = Actualidad.objects.get(id = id).delete()
	return HttpResponseRedirect('/alianzas/actualidad/')


def foros_list(request, template = 'admin/foros_list.html'):
	list_object_forum = Foros.objects.filter(usuario = request.user.id)
	return render(request,template,locals())

@login_required
def foros_crear(request,template = 'admin/foro.html'):
	if request.method == 'POST':
		form = ForoForm(request.POST, request.FILES)
		usuarios = User.objects.filter(organizacion__isnull = False)
		if form.is_valid():
			foro = form.save(commit=False)
			foro.usuario = request.user
			foro.aprobado = False
			foro.save()
			foro.usuarios_siguiendo.set(usuarios)
			form.save_m2m()
			
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/foro.txt', {'obj': foro,})

				html_content = render_to_string('email/foro.txt', {'obj': foro,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return redirect('/alianzas/foros/'+'?new=foro_nuevo')
			except:
				pass
	else:
		form = ForoForm()

	return render(request, template, locals())

@login_required
def foros_editar(request, id, template = 'admin/foro.html'):
	object = get_object_or_404(Foros, id=id)
	if request.method == 'POST':
		form = ForoForm(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.usuario = request.user
			form_uncommited.save()
			return HttpResponseRedirect('/alianzas/foros/')
	else:
		form = ForoForm(instance=object)

	return render(request, template, locals())

@login_required
def foro_eliminar(request,id):
	foro = Foros.objects.get(id = id).delete()
	return HttpResponseRedirect('/alianzas/foros/')

@login_required
def events_list(request,template = 'admin/iniciativas-destacadas.html'):
	list_object_events = Evento.objects.filter(author = request.user.id)
	campanias = Actualidad.objects.filter(author = request.user.id,category = 'campanas')
	concursos = Actualidad.objects.filter(author = request.user.id,category = 'concursos')

	return render(request,template,locals())

@login_required
def events_crear(request,template = 'admin/event.html'):
	FormSetInit = inlineformset_factory(Evento,GaleriaEventos,form=GaleriaEventosForm,extra=1)
	if request.method == 'POST':
		form = EventsForms(request.POST, request.FILES)
		formset = FormSetInit(request.POST, request.FILES)
		if form.is_valid() and formset.is_valid():
			event = form.save(commit=False)
			event.author = request.user
			event.aprobado = False
			event.save()
			form.save_m2m()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.evento = event
				instance.save()
			formset.save_m2m()
			
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/evento.txt', {'obj': event,})

				html_content = render_to_string('email/evento.txt', {'obj': event,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return redirect('/alianzas/iniciativas-destacadas/'+'?tab=eventos'+'?new=new_evento')
			except:
				pass
	else:
		form = EventsForms()
		formset = FormSetInit()

	return render(request, template, locals())

@login_required
def events_editar(request, id, template = 'admin/event.html'):
	object = get_object_or_404(Evento, id=id)
	FormSetInit = inlineformset_factory(Evento,GaleriaEventos,form=GaleriaEventosForm,extra=1)
	if request.method == 'POST':
		form = EventsForms(request.POST, request.FILES, instance=object)
		formset = FormSetInit(request.POST, request.FILES, instance=object)
		if form.is_valid() and formset.is_valid():
			form_uncommited = form.save()
			form_uncommited.author = request.user
			form_uncommited.save()
			formset.save()
			return redirect('/alianzas/iniciativas-destacadas/'+'?tab=eventos')
	else:
		form = EventsForms(instance=object)
		formset = FormSetInit(instance=object)

	return render(request, template, locals())

@login_required
def events_eliminar(request, id):
	nota = Evento.objects.get(id = id).delete()
	return redirect('/alianzas/iniciativas-destacadas/'+'?tab=eventos')

@login_required
def recursos_list(request,template='admin/recursos.html'):
	list_objects_imagenes = GaleriaImagenes.objects.filter(usuario = request.user.id)
	list_objects_video = GaleriaVideos.objects.filter(usuario = request.user.id)
	list_objects_audio = Audios.objects.filter(usuario = request.user.id)
	publicaciones = Publicacion.objects.filter(usuario = request.user.id, tipo = 1)
	guias = Publicacion.objects.filter(usuario = request.user.id, tipo = 2)

	return render(request,template,locals())

@login_required
def publicacion_agregar(request, template = 'admin/publicaciones.html'):
	FormSetInit = inlineformset_factory(Publicacion,ArchivosPublicacion,form=ArchivosPublicacionForm,extra=1)
	# FormSetInit2 = inlineformset_factory(Publicacion,AudiosPublicacion,form=AudiosPublicacionForm,extra=1)
	# FormSetInit3 = inlineformset_factory(Publicacion,VideosPublicacion,form=VideosPublicacionForm,extra=1)
	if request.method == 'POST':
		form = PublicacionForm(request.POST, request.FILES)
		formset = FormSetInit(request.POST,request.FILES)
		# formset2 = FormSetInit2(request.POST,request.FILES)
		# formset3 = FormSetInit3(request.POST)
		if form.is_valid() and formset.is_valid(): # and formset2.is_valid() and formset3.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.usuario = request.user
			form_uncommited.tipo = 1
			form_uncommited.aprobado = False
			form_uncommited.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.publicacion = form_uncommited
				instance.save()
			formset.save_m2m()

			# instances2 = formset2.save(commit=False)
			# for instance in instances2:
			# 	instance.publicacion = form_uncommited
			# 	instance.save()
			# formset2.save_m2m()

			# instances3 = formset3.save(commit=False)
			# for instance in instances3:
			# 	instance.publicacion = form_uncommited
			# 	instance.save()
			# formset3.save_m2m()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/publicacion.txt', {'obj': form_uncommited,})

				html_content = render_to_string('email/publicacion.txt', {'obj': form_uncommited,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return redirect('/alianzas/recursos-metodologicos/'+'?tab=publicaciones'+'?new=new_pub')
			except:
				pass

	else:
		form = PublicacionForm()
		formset = FormSetInit()
		# formset2 = FormSetInit2()
		# formset3 = FormSetInit3()

	return render(request,template,locals())

@login_required
def publicacion_editar(request, id, template = 'admin/publicaciones.html'):
	object = get_object_or_404(Publicacion, id=id)
	FormSetInit = inlineformset_factory(Publicacion,ArchivosPublicacion,form=ArchivosPublicacionForm,extra=1)
	# FormSetInit2 = inlineformset_factory(Publicacion,AudiosPublicacion,form=AudiosPublicacionForm,extra=1)
	# FormSetInit3 = inlineformset_factory(Publicacion,VideosPublicacion,form=VideosPublicacionForm,extra=1)
	if request.method == 'POST':
		form = PublicacionForm(request.POST, request.FILES, instance=object)
		formset = FormSetInit(request.POST,request.FILES, instance=object)
		# formset2 = FormSetInit2(request.POST,request.FILES, instance=object)
		# formset3 = FormSetInit3(request.POST, instance=object)
		if form.is_valid() and formset.is_valid(): # and formset2.is_valid() and formset3.is_valid():
			form_uncommited = form.save()
			form_uncommited.save()

			formset.save()

			# formset2.save()

			# formset3.save()

			return redirect('/alianzas/recursos-metodologicos/'+'?tab=publicaciones')
	else:
		form = PublicacionForm(instance=object)
		formset = FormSetInit(instance=object)
		# formset2 = FormSetInit2(instance=object)
		# formset3 = FormSetInit3(instance=object)

	return render(request,template,locals())

@login_required
def guia_agregar(request, template = 'admin/publicaciones.html'):
	FormSetInit = inlineformset_factory(Publicacion,ArchivosPublicacion,form=ArchivosPublicacionForm,extra=1)
	FormSetInit2 = inlineformset_factory(Publicacion,AudiosPublicacion,form=AudiosPublicacionForm,extra=1)
	FormSetInit3 = inlineformset_factory(Publicacion,VideosPublicacion,form=VideosPublicacionForm,extra=1)
	if request.method == 'POST':
		form = PublicacionForm(request.POST, request.FILES)
		formset = FormSetInit(request.POST,request.FILES)
		formset2 = FormSetInit2(request.POST,request.FILES)
		formset3 = FormSetInit3(request.POST)
		if form.is_valid() and formset.is_valid() and formset2.is_valid() and formset3.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.usuario = request.user
			form_uncommited.tipo = 2
			form_uncommited.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.publicacion = form_uncommited
				instance.save()
			formset.save_m2m()

			instances2 = formset2.save(commit=False)
			for instance in instances2:
				instance.publicacion = form_uncommited
				instance.save()
			formset2.save_m2m()

			instances3 = formset3.save(commit=False)
			for instance in instances3:
				instance.publicacion = form_uncommited
				instance.save()
			formset3.save_m2m()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/guia.txt', {'obj': form_uncommited,})

				html_content = render_to_string('email/guia.txt', {'obj': form_uncommited,})

				list_mail = User.objects.filter(organizacion__isnull = False).exclude(id = request.user.id).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return HttpResponseRedirect('/alianzas/recursos-metodologicos/')
			except:
				pass

	else:
		form = PublicacionForm()
		formset = FormSetInit()
		formset2 = FormSetInit2()
		formset3 = FormSetInit3()

	return render(request,template,locals())

@login_required
def publicacion_eliminar(request,id):
	publicacion = Publicacion.objects.get(id=id).delete()
	return redirect('/alianzas/recursos-metodologicos/'+'?tab=publicaciones')

@login_required
def galeria_img_crear(request,template = 'admin/galeria_img.html'):
	FormSetInit = inlineformset_factory(GaleriaImagenes, Imagenes, form=ImagenesForm,extra=1)
	if request.method == 'POST':
		form = GaleriaImagenesForm(request.POST, request.FILES)
		formset = FormSetInit(request.POST,request.FILES)
		if form.is_valid() and formset.is_valid():
			galeria = form.save(commit=False)
			galeria.usuario = request.user
			galeria.aprobado = False
			galeria.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.imagenes = galeria
				instance.save()
			formset.save_m2m()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/galeria.txt', {'obj': galeria,})

				html_content = render_to_string('email/galeria.txt', {'obj': galeria,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return redirect('/alianzas/recursos-metodologicos/'+'?tab=imagenes'+'?new=new_img')
			except:
				pass
	else:
		form = GaleriaImagenesForm()
		formset = FormSetInit()

	return render(request, template, locals())

@login_required
def galeria_img_editar(request, id, template = 'admin/galeria_img.html'):
	object = get_object_or_404(GaleriaImagenes, id=id)
	FormSetInit = inlineformset_factory(GaleriaImagenes, Imagenes, form=ImagenesForm,extra=1)
	if request.method == 'POST':
		form = GaleriaImagenesForm(data=request.POST,instance=object,files=request.FILES)
		formset = FormSetInit(request.POST,request.FILES,instance=object)

		if form.is_valid() and formset.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.save()

			formset.save()
			return redirect('/alianzas/recursos-metodologicos/'+'?tab=imagenes')
	else:
		form = GaleriaImagenesForm(instance=object)
		formset = FormSetInit(instance=object)

	return render(request, template, locals())

@login_required
def galeria_img_eliminar(request,id):
	galeria_img = GaleriaImagenes.objects.get(id=id).delete()
	return redirect('/alianzas/recursos-metodologicos/'+'?tab=imagenes')

@login_required
def galeria_vid_crear(request,template = 'admin/galeria_vid.html'):
	FormSetInit = inlineformset_factory(GaleriaVideos, ListVideos, form=ListVideosForm,extra=1)
	if request.method == 'POST':
		form = GaleriaVideosForm(request.POST, request.FILES)
		formset = FormSetInit(request.POST,request.FILES)
		if form.is_valid() and formset.is_valid():
			video = form.save(commit=False)
			video.usuario = request.user
			video.aprobado = False
			video.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.videos = video
				instance.save()
			formset.save_m2m()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/video.txt', {'obj': video,})

				html_content = render_to_string('email/video.txt', {'obj': video,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return redirect('/alianzas/recursos-metodologicos/'+'?tab=videos'+'?new=new_vid')
			except:
				pass

	else:
		form = GaleriaVideosForm()
		formset = FormSetInit()

	return render(request, template, locals())

@login_required
def galeria_vid_editar(request, id, template = 'admin/galeria_vid.html'):
	object = get_object_or_404(GaleriaVideos, id=id)
	FormSetInit = inlineformset_factory(GaleriaVideos, ListVideos, form=ListVideosForm,extra=1)
	if request.method == 'POST':
		form = GaleriaVideosForm(request.POST, request.FILES, instance=object)
		formset = FormSetInit(request.POST,request.FILES, instance=object)
		if form.is_valid() and formset.is_valid():
			video = form.save(commit=False)
			video.save()

			formset.save()

			return redirect('/alianzas/recursos-metodologicos/'+'?tab=videos')
	else:
		form = GaleriaVideosForm(instance=object)
		formset = FormSetInit(instance=object)
	return render(request,template,locals())

@login_required
def galeria_vid_eliminar(request,id):
	galeria_vid = GaleriaVideos.objects.get(id=id).delete()
	return redirect('/alianzas/recursos-metodologicos/'+'?tab=videos')

@login_required
def galeria_audio_crear(request,template = 'admin/galeria_audio.html'):
	FormSetInit = inlineformset_factory(Audios, ListAudios, form=ListAudiosForm,extra=1)
	if request.method == 'POST':
		form = AudiosForm(request.POST, request.FILES)
		formset = FormSetInit(request.POST,request.FILES)
		if form.is_valid() and formset.is_valid():
			audio = form.save(commit=False)
			audio.usuario = request.user
			audio.aprobado = False
			audio.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.audios = audio
				instance.save()
			formset.save_m2m()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/audio.txt', {'obj': audio,})

				html_content = render_to_string('email/audio.txt', {'obj': audio,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return redirect('/alianzas/recursos-metodologicos/'+'?tab=audios'+'?new=new_aud')
			except:
				pass

	else:
		form = AudiosForm()
		formset = FormSetInit()

	return render(request, template, locals())

@login_required
def galeria_audio_editar(request, id, template = 'admin/galeria_audio.html'):
	object = get_object_or_404(Audios, id=id)
	FormSetInit = inlineformset_factory(Audios, ListAudios, form=ListAudiosForm,extra=1)
	if request.method == 'POST':
		form = AudiosForm(request.POST, request.FILES, instance=object)
		formset = FormSetInit(request.POST,request.FILES, instance=object)
		if form.is_valid() and formset.is_valid():
			audio = form.save(commit=False)
			audio.save()

			formset.save()

			return redirect('/alianzas/recursos-metodologicos/'+'?tab=audios')
	else:
		form = AudiosForm(instance=object)
		formset = FormSetInit(instance=object)

	return render(request,template,locals())

@login_required
def galeria_audio_eliminar(request,id):
	galeria_vid = Audios.objects.get(id=id).delete()
	return redirect('/alianzas/recursos-metodologicos/'+'?tab=audios')

#Puntos de vista
@login_required
def puntos_vista_list(request,template = 'admin/puntos_list.html'):
	list_object_puntos = Puntos.objects.filter(usuario = request.user.id)
	return render(request,template,locals())

@login_required
def puntos_vista_crear(request,template = 'admin/punto.html'):
	FormSetInit = inlineformset_factory(Puntos,GaleriaPuntos,form=GaleriaPuntosForm,extra=1)
	if request.method == 'POST':
		form = PuntosForms(request.POST, request.FILES)
		formset = FormSetInit(request.POST, request.FILES)
		if form.is_valid() and formset.is_valid():
			punto = form.save(commit=False)
			punto.usuario = request.user
			punto.aprobado = False
			punto.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.punto = punto
				instance.save()
			formset.save_m2m()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/punto.txt', {'obj': punto,})

				html_content = render_to_string('email/punto.txt', {'obj': punto,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				
			except:
				pass
				
			return redirect('/alianzas/puntos-vista/'+'?new=punto_nuevo')
			
	else:
		form = PuntosForms()
		formset = FormSetInit()

	return render(request, template, locals())

@login_required
def puntos_vista_edit(request,slug,template = 'admin/punto.html'):
	object = get_object_or_404(Puntos, slug=slug)
	FormSetInit = inlineformset_factory(Puntos,GaleriaPuntos,form=GaleriaPuntosForm,extra=1)
	if request.method == 'POST':
		form = PuntosForms(request.POST, request.FILES, instance = object)
		formset = FormSetInit(request.POST, request.FILES, instance=object)
		if form.is_valid() and formset.is_valid():
			puntos = form.save()
			puntos.usuario = request.user
			puntos.save()
			formset.save()
			return HttpResponseRedirect('/alianzas/puntos-vista/')
	else:
		form = PuntosForms(instance = object)
		formset = FormSetInit(instance = object)

	return render(request,template,locals())

@login_required
def puntos_vista_eliminar(request,id):
	puntos_vista = Puntos.objects.get(id = id).delete()
	return HttpResponseRedirect('/alianzas/puntos-vista/')

@login_required
def campanias_crear(request,template = 'admin/actualidad.html'):
	FormSetInit = inlineformset_factory(Actualidad,Galeria,form=GaleriaForm,extra=1)		
	if request.method == 'POST':
		form = Actualidad2Forms(request.POST, request.FILES)
		formset = FormSetInit(request.POST, request.FILES)
		if form.is_valid() and formset.is_valid():
			campanias = form.save(commit=False)
			campanias.author = request.user
			campanias.category = 'campanas'
			campanias.aprobado = False
			campanias.save()
			form.save_m2m()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.actualidad = campanias
				instance.save()
			formset.save_m2m()

			
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/campanias.txt', {'obj': campanias,})

				html_content = render_to_string('email/campanias.txt', {'obj': campanias,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return redirect('/alianzas/iniciativas-destacadas/'+'?tab=campana'+'?new=new_camp')
			except:
				pass
	else:
		form = Actualidad2Forms()
		formset = FormSetInit()

	return render(request, template, locals())

@login_required
def campanias_editar(request, id, template = 'admin/actualidad.html'):
	object = get_object_or_404(Actualidad, id=id)
	if request.method == 'POST':
		form = Actualidad2Forms(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.author = request.user
			form_uncommited.save()
			return redirect('/alianzas/iniciativas-destacadas/'+'?tab=campana')
	else:
		form = Actualidad2Forms(instance=object)
	return render(request, template, locals())

@login_required
def eliminar_campania(request, id):
	camp = Actualidad.objects.get(id = id).delete()
	return redirect('/alianzas/iniciativas-destacadas/'+'?tab=campana')

@login_required
def concursos_crear(request,template = 'admin/actualidad.html'):
	FormSetInit = inlineformset_factory(Actualidad,Galeria,form=GaleriaForm,extra=1)
	if request.method == 'POST':
		form = Actualidad2Forms(request.POST, request.FILES)
		formset = FormSetInit(request.POST, request.FILES)
		if form.is_valid() and form.is_valid():
			concurso = form.save(commit=False)
			concurso.author = request.user
			concurso.category = 'concursos'
			concurso.aprobado = False
			concurso.save()
			form.save_m2m()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.actualidad = concurso
				instance.save()
			formset.save_m2m()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/concursos.txt', {'obj': concurso,})

				html_content = render_to_string('email/concursos.txt', {'obj': concurso,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return redirect('/alianzas/iniciativas-destacadas/'+'?tab=concursos'+'?new=new_conc')
			except:
				pass
	else:
		form = Actualidad2Forms()
		formset = FormSetInit()

	return render(request, template, locals())

@login_required
def concursos_editar(request, id, template = 'admin/actualidad.html'):
	object = get_object_or_404(Actualidad, id=id)
	if request.method == 'POST':
		form = Actualidad2Forms(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.author = request.user
			form_uncommited.save()
			return redirect('/alianzas/iniciativas-destacadas/'+'?tab=concursos')
	else:
		form = Actualidad2Forms(instance=object)
	return render(request, template, locals())

@login_required
def eliminar_concursos(request, id):
	concurso = Actualidad.objects.get(id = id).delete()
	return redirect('/alianzas/iniciativas-destacadas/'+'?tab=concursos')

