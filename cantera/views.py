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

def index(request,template='index.html'):
	# actualidad = Actualidad.objects.order_by('-created_on')[:6]
	actualidad = Actualidad.objects.filter(category__in = ['noticias','situacion-regional-genero'],aprobado = True).order_by('-created_on')[:6]
	hoy = datetime.date.today()
	eventos = Evento.objects.filter(inicio__gte = hoy,aprobado = True).order_by('-inicio','-hora_inicio')[:3]
	foros = Foros.objects.filter(aprobado = True).annotate(conteo = Count('aportes')).order_by('-conteo','-aportes__fecha')[:3]
	alianzas = Contraparte.objects.order_by('nombre').exclude(nombre = 'Particular')
	slider = Slider.objects.all()
	compromisos = Compromiso.objects.aggregate(total = Sum('conteo_hombres') + Sum('conteo_mujeres'))['total']
	
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