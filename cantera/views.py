from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from organizaciones.models import *
from organizaciones.forms import *
from actualidad.models import *
from evento.models import *
from configuracion.models import *
from foro.models import *
import datetime
from django.db.models import Count, Sum
from users.models import *
from users.forms import *
from solicitudes.models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from compromisos.models import *
from configuracion.models import InformacionDestacada
from django.db.models import Q
from puntosvista.models import *
import random
from publicaciones.models import *
from galerias.models import *
from evento.models import *

def index(request,template='index.html'):
	# actualidad = Actualidad.objects.order_by('-created_on')[:6]
	actualidad = Actualidad.objects.filter(category__in = ['noticias','situacion-regional-genero'],aprobado = True).order_by('-created_on')[:6]
	hoy = datetime.date.today()
	eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio','-hora_inicio')[:3]
	foros = Foros.objects.filter(aprobado = True).annotate(conteo = Count('aportes')).order_by('-conteo','-aportes__fecha')[:3]
	alianzas = Contraparte.objects.order_by('nombre').exclude(nombre = 'Particular')
	slider = Slider.objects.all()
	compromisos = Compromiso.objects.aggregate(total = Sum('conteo_hombres') + Sum('conteo_mujeres'))['total']
	hombres = Compromiso.objects.aggregate(total = Sum('conteo_hombres'))['total']
	mujeres = Compromiso.objects.aggregate(total = Sum('conteo_mujeres'))['total']
	
	return render(request, template,locals())

@login_required
def perfil(request,template='admin/org_index.html'):
	# try:
	organizacion = Contraparte.objects.get(id = request.user.organizacion.id)
	if request.method == 'POST':
		form = SolicitudOrgForm(request.POST)
		form2 = SolicitudesNuevasOrgForm(request.POST)
		if form.is_valid():
			solicitud = form.save(commit=False)
			solicitud.usuario = request.user
			solicitud.aprobado = False
			solicitud.save()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/vincular_org.txt', {'obj': solicitud,})

				html_content = render_to_string('email/vincular_org.txt', {'obj': solicitud,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return HttpResponseRedirect('/accounts/profile/')
			except:
				pass

		if form2.is_valid():
			nueva_org = form2.save(commit=False)
			nueva_org.usuario = request.user
			nueva_org.aprobado = False
			nueva_org.save()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/new_org.txt', {'obj': nueva_org,})

				html_content = render_to_string('email/new_org.txt', {'obj': nueva_org,})

				list_mail = User.objects.filter(is_superuser = True).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return HttpResponseRedirect('/accounts/profile/')
			except:
				pass
	else:
		form = SolicitudOrgForm()
		form2 = SolicitudesNuevasOrgForm(request.POST)
		solicitud_peniente = SolicitudesOrg.objects.filter(usuario = request.user,aprobado = False)
		solicitud_nueva_org = SolicitudesNuevasOrg.objects.filter(usuario = request.user,aprobado = False)

	return render(request, template,locals())
	# except :
	# 	return render(request, 'admin/error.html',locals())

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


from allauth.account.views import PasswordChangeView, SignupView

class CustomPasswordChangeView(PasswordChangeView):
	@property
	def success_url(self):
		return '/'


class LocaLSignupView(SignupView):
    success_url = '/'

def buscador_general(request,template='buscador_general.html'):
	hoy = datetime.date.today()
	if request.GET.get('q'):
		q = request.GET['q']
		list_object = []
		#actualidad
		actualidad = Actualidad.objects.filter(
										Q(tittle__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										aprobado = True,
										created_on__lte = hoy).order_by('-created_on')
		for obj in actualidad:
			list_object.append((obj.tittle,obj.content,obj.get_absolute_url()))
		
		#puntos vista
		puntos_vista = Puntos.objects.filter(
										Q(tittle__icontains = q) |
										Q(contenido__icontains = q),aprobado = True,fecha_creacion__lte = hoy).order_by('tittle')
		for obj in puntos_vista:
			list_object.append((obj.tittle,obj.contenido,obj.get_absolute_url()))

		#foros
		foros = Foros.objects.filter(
										Q(nombre__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(contenido__icontains = q),aprobado = True).order_by('-creacion')
		for obj in foros:
			list_object.append((obj.nombre,obj.contenido,obj.get_absolute_url()))
		
		#publicaciones
		publicaciones = Publicacion.objects.filter(
										Q(titulo__icontains = q) |
										Q(resumen__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(tags__name__icontains = q),
										aprobado = True).distinct('id').order_by('-id')
		for obj in publicaciones:
			list_object.append((obj.titulo,obj.resumen,obj.get_absolute_url()))

		#galerias-img
		galerias_img = GaleriaImagenes.objects.filter(
												Q(titulo__icontains = q) |
												Q(descripcion__icontains = q) |
												Q(tematica__nombre__icontains = q),aprobado = True).distinct('id').order_by('-id')
		for obj in galerias_img:
			list_object.append((obj.titulo,obj.descripcion,obj.get_absolute_url()))
		
		#galerias-videos
		galerias_videos = GaleriaVideos.objects.filter(
												Q(titulo__icontains = q) |
												Q(descripcion__icontains = q) |
												Q(tematica__nombre__icontains = q),aprobado = True).distinct('id').order_by('-id')
		for obj in galerias_videos:
			list_object.append((obj.titulo,obj.descripcion,obj.get_absolute_url()))
		
		#audios
		audios = Audios.objects.filter(
										Q(titulo__icontains = q) |
										Q(descripcion__icontains = q) |
										Q(tematica__nombre__icontains = q),aprobado = True).distinct('id').order_by('-id')
		for obj in audios:
			list_object.append((obj.titulo,obj.descripcion,obj.get_absolute_url()))
		
		#eventos
		evento = Evento.objects.filter(
										Q(tittle__icontains = q) |
										Q(descripcion__icontains = q) |
										Q(tags__name__icontains = q),aprobado = True).distinct('id').order_by('-id')
		for obj in evento:
			list_object.append((obj.tittle,obj.descripcion,obj.get_absolute_url()))

		#random list
		random.shuffle(list_object)
	else:
		list_object = []
		
	return render(request,template,locals())