from django.contrib import admin
from .models import *
from users.models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.
class GaleriaInline(admin.TabularInline):
	model = Galeria
	extra = 1

class ActualidadAdmin(admin.ModelAdmin):
	inlines = [GaleriaInline,]

	def save_model(self, request, obj, form, change):
		if obj.aprobado == True and obj.category != 'situacion-regional-genero':
			try:
				subject, from_email = 'Plataforma Género y Metodologías', 'generoymetodologias@gmail.com'
				if obj.category == 'noticias':
					text_content =  render_to_string('email/aprobacion.txt', {'obj': obj,})

					html_content = render_to_string('email/aprobacion.txt', {'obj': obj,})
				elif obj.category == 'campanas':
					text_content =  render_to_string('email/aprobacion_camp.txt', {'obj': obj,})

					html_content = render_to_string('email/aprobacion_camp.txt', {'obj': obj,})
				elif obj.category == 'concursos':
					text_content =  render_to_string('email/aprobacion_conc.txt', {'obj': obj,})

					html_content = render_to_string('email/aprobacion_conc.txt', {'obj': obj,})

				user = User.objects.get(id = obj.author.id)
				list_mail = [user.email,]

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
			except:
				pass
		super().save_model(request, obj, form, change)

admin.site.register(Actualidad,ActualidadAdmin)
admin.site.register(Temas)

#paginas estaticas
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
 
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
 
class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = FlatPage
        fields = '__all__'
 
 
class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm
 
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)