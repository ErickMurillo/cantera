from django.contrib import admin
from .models import *
from users.models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.

class SolicitudesOrgAdmin(admin.ModelAdmin):
	list_display = ('usuario','organizacion','aprobado')

	def add_view(self, request, form_url='', extra_context=None):
		self.readonly_fields = ('usuario','organizacion','aprobado')
		return super(SolicitudesOrgAdmin, self).add_view(request)

	def change_view(self,request, object_id, form_url='', extra_context=None):
		obj = SolicitudesOrg.objects.get(id = object_id)
		if obj.aprobado == False:
			self.readonly_fields = ('usuario','organizacion')
		else:
			self.readonly_fields = ('usuario','organizacion','aprobado')
		return super(SolicitudesOrgAdmin, self).change_view(request,object_id)

	def save_model(self, request, obj, form, change):
		if obj.aprobado == True:
			user = User.objects.get(id = obj.usuario.id)
			user.organizacion = obj.organizacion
			user.save()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/solicitud_aprobada.txt', {'obj': user,})

				html_content = render_to_string('email/solicitud_aprobada.txt', {'obj': user,})

				list_mail = User.objects.filter(id = user.id).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
			except:
				pass

		super(SolicitudesOrgAdmin, self).save_model(request, obj, form, change)

	def has_delete_permission(self, request, obj=None):
		return False

class SolicitudesNuevasOrgAdmin(admin.ModelAdmin):
	list_display = ('usuario','nombre_org','aprobado')

	def add_view(self, request, form_url='', extra_context=None):
		self.readonly_fields = ('usuario','nombre_org','siglas_org','pais_org','aprobado')
		return super(SolicitudesNuevasOrgAdmin, self).add_view(request)

	def change_view(self, request, object_id, form_url='', extra_context=None):
		obj = SolicitudesNuevasOrg.objects.get(id = object_id)
		if obj.aprobado == False:
			self.readonly_fields = ('usuario','nombre_org','siglas_org','pais_org')
		else:
			self.readonly_fields = ('usuario','nombre_org','siglas_org','pais_org','aprobado')
		return super(SolicitudesNuevasOrgAdmin, self).change_view(request,object_id)

	def save_model(self, request, obj, form, change):
		if obj.aprobado == True:
			org = Contraparte(nombre = obj.nombre_org,siglas = obj.siglas_org,pais = obj.pais_org)
			org.save()
			user = User.objects.get(id = obj.usuario.id)
			user.organizacion = org
			user.save()

			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/solicitud_aprobada.txt', {'obj': user,})

				html_content = render_to_string('email/solicitud_aprobada.txt', {'obj': user,})

				list_mail = User.objects.filter(id = user.id).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
			except:
				pass

		super(SolicitudesNuevasOrgAdmin, self).save_model(request, obj, form, change)

	def has_delete_permission(self, request, obj=None):
		return False

admin.site.register(SolicitudesOrg,SolicitudesOrgAdmin)
admin.site.register(SolicitudesNuevasOrg,SolicitudesNuevasOrgAdmin)
