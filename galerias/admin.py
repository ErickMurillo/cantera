from django.contrib import admin
from .models import *
from users.models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from rangefilter.filter import DateRangeFilter

# Register your models here.
class ImagenesInline(admin.TabularInline):
	model = Imagenes
	extra = 1

class GaleriaImagenesAdmin(admin.ModelAdmin):
	inlines = [ImagenesInline,]
	list_display = ('titulo','tematica','aprobado','created_on')
	list_filter = ('tematica','aprobado',('created_on', DateRangeFilter),)
	search_fields = ['titulo',]

	def save_model(self,request,obj,form,change):
		if obj.aprobado == True and obj.usuario != request.user:
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/aprobacion_img.txt', {'obj': obj,})

				html_content = render_to_string('email/aprobacion_img.txt', {'obj': obj,})

				user = User.objects.get(id = obj.usuario.id)
				list_mail = [user.email,]

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
			except:
				pass
		super().save_model(request, obj, form, change)

class ListVideosInline(admin.TabularInline):
	model = ListVideos
	extra = 1

class GaleriaVideosAdmin(admin.ModelAdmin):
	inlines = [ListVideosInline]
	list_display = ('titulo','tematica','aprobado','created_on')
	list_filter = ('tematica','aprobado',('created_on', DateRangeFilter),)
	search_fields = ['titulo',]

	def save_model(self,request,obj,form,change):
		if obj.aprobado == True and obj.usuario != request.user:
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/aprobacion_vid.txt', {'obj': obj,})

				html_content = render_to_string('email/aprobacion_vid.txt', {'obj': obj,})

				user = User.objects.get(id = obj.usuario.id)
				list_mail = [user.email,]

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
			except:
				pass
		super().save_model(request, obj, form, change)

class ListAudiosInline(admin.TabularInline):
	model = ListAudios
	extra = 1

class AudiosAdmin(admin.ModelAdmin):
	inlines = [ListAudiosInline]
	list_display = ('titulo','tematica','aprobado','created_on')
	list_filter = ('tematica','aprobado',('created_on', DateRangeFilter),)
	search_fields = ['titulo',]

	def save_model(self,request,obj,form,change):
		if obj.aprobado == True and obj.usuario != request.user:
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/aprobacion_aud.txt', {'obj': obj,})

				html_content = render_to_string('email/aprobacion_aud.txt', {'obj': obj,})

				user = User.objects.get(id = obj.usuario.id)
				list_mail = [user.email,]

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
			except:
				pass
		super().save_model(request, obj, form, change)

admin.site.register(GaleriaImagenes,GaleriaImagenesAdmin)
admin.site.register(GaleriaVideos,GaleriaVideosAdmin)
admin.site.register(Audios,AudiosAdmin)