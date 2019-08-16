from django.contrib import admin
from .models import *
import nested_admin
from users.models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# class ComentariosInline(nested_admin.NestedStackedInline):
# 	model = Comentarios
# 	extra = 1

# class AportesInline(nested_admin.NestedStackedInline):
# 	model = Aportes
# 	inlines = [ComentariosInline,]
# 	extra = 1

class ForosAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		if obj.aprobado == True and obj.usuario != request.user:
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				text_content =  render_to_string('email/aprobacion_foro.txt', {'obj': obj,})

				html_content = render_to_string('email/aprobacion_foro.txt', {'obj': obj,})

				user = User.objects.get(id = obj.usuario.id)
				list_mail = [user.email,]

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
			except:
				pass
		super().save_model(request, obj, form, change)


admin.site.register(Foros,ForosAdmin)
admin.site.register(Aportes)
admin.site.register(Comentarios)