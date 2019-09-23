from django.contrib import admin
from .models import *
from users.models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.
class GaleriaInline(admin.TabularInline):
	model = GaleriaEventos
	extra = 1

class EventoAdmin(admin.ModelAdmin):
	inlines = [GaleriaInline,]
	
	def save_model(self,request,obj,form,change):
		if obj.aprobado == True and obj.author != request.user:
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/aprobacion_evento.txt', {'obj': obj,})

				html_content = render_to_string('email/aprobacion_evento.txt', {'obj': obj,})

				user = User.objects.get(id = obj.author.id)
				list_mail = [user.email,]

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
			except:
				pass
		super().save_model(request, obj, form, change)

admin.site.register(Evento,EventoAdmin)
