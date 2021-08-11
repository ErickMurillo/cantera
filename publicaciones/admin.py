from django.contrib import admin
from .models import *
from users.models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.
class ArchivosPublicacionInline(admin.TabularInline):
	model = ArchivosPublicacion
	extra = 1

class AudiosPublicacionInline(admin.TabularInline):
	model = AudiosPublicacion
	extra = 1

class VideosPublicacionInline(admin.TabularInline):
	model = VideosPublicacion
	extra = 1

class PublicacionAdmin(admin.ModelAdmin):
	inlines = [ArchivosPublicacionInline,]
	
	def save_model(self,request,obj,form,change):
		if obj.aprobado == True and obj.usuario != request.user:
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/aprobacion_pub.txt', {'obj': obj,})

				html_content = render_to_string('email/aprobacion_pub.txt', {'obj': obj,})

				user = User.objects.get(id = obj.usuario.id)
				list_mail = [user.email,]

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
			except:
				pass
		super().save_model(request, obj, form, change)

admin.site.register(Publicacion,PublicacionAdmin)