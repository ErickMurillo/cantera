from django.contrib import admin
from .models import *
from users.models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from rangefilter.filter import DateRangeFilter
from django.utils.html import format_html

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

class PreguntasPublicacionInline(admin.TabularInline):
	model = PreguntasPublicacion
	extra = 1

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import path, reverse

class PublicacionDetailView(PermissionRequiredMixin, DetailView):
	permission_required = "publicacion.view_order"
	template_name = "admin/publicaciones/preguntas.html"
	model = Publicacion

	def get_context_data(self, **kwargs):
		id = self.request.resolver_match.kwargs.get('pk')
		preg = {}
		for x in RespMaterial.objects.all():
			p = PreguntasPublicacion.objects.filter(utilizara_material = x,publicacion = id).count()
			preg[x] = p

		preg2 = {}
		for x in PERFIL_CHOICES:
			p = PreguntasPublicacion.objects.filter(perfil = x[0],publicacion = id).count()
			preg2[x[1]] = p

		return {
			**super().get_context_data(**kwargs),
			**admin.site.each_context(self.request),
			"opts": self.model._meta,
			"resp1": preg,
			"resp2": preg2,
		}

class PreguntasDashboardView(PermissionRequiredMixin, TemplateView):
	permission_required = "publicacion.view_order"
	template_name = "admin/publicaciones/dashboard.html"

	def get_context_data(self, **kwargs):
		fecha_inicio = self.request.GET.get('fecha_inicio') or ''
		fecha_fin = self.request.GET.get('fecha_fin') or ''

		qs = PreguntasPublicacion.objects.all()
		if fecha_inicio:
			qs = qs.filter(publicacion__created_on__gte = fecha_inicio)
		if fecha_fin:
			qs = qs.filter(publicacion__created_on__lte = fecha_fin)

		material_labels = []
		material_data = []
		for x in RespMaterial.objects.all():
			material_labels.append(x.nombre)
			material_data.append(qs.filter(utilizara_material = x).count())

		perfil_labels = []
		perfil_data = []
		for value, label in PERFIL_CHOICES:
			perfil_labels.append(label)
			perfil_data.append(qs.filter(perfil = value).count())

		return {
			**super().get_context_data(**kwargs),
			**admin.site.each_context(self.request),
			"opts": Publicacion._meta,
			"title": "Dashboard de encuestas",
			"fecha_inicio": fecha_inicio,
			"fecha_fin": fecha_fin,
			"material_labels": material_labels,
			"material_data": material_data,
			"material_pairs": list(zip(material_labels, material_data)),
			"perfil_labels": perfil_labels,
			"perfil_data": perfil_data,
			"perfil_pairs": list(zip(perfil_labels, perfil_data)),
			"total_respuestas": qs.count(),
		}

class PublicacionAdmin(admin.ModelAdmin):
	inlines = [ArchivosPublicacionInline]
	list_display = ('titulo','tipo','tematica','usuario','aprobado','created_on','preguntas')
	list_filter = ('tipo','tematica','aprobado',('created_on', DateRangeFilter),)
	search_fields = ['titulo',]
	change_list_template = "admin/publicaciones/publicacion_change_list.html"

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
	
	def get_urls(self):
		return [
			path(
				"dashboard-preguntas/",
				self.admin_site.admin_view(PreguntasDashboardView.as_view()),
				name="preguntas_dashboard",
			),
			path(
				"<pk>/detail",
				self.admin_site.admin_view(PublicacionDetailView.as_view()),
				name=f"publicacion_detail",
			),
			*super().get_urls(),
		]
	
	def preguntas(self, obj: Publicacion) -> str:
		url = reverse("admin:publicacion_detail", args=[obj.pk])
		return format_html(f'<a href="{url}">Detalle</a>')

admin.site.register(Publicacion,PublicacionAdmin)

admin.site.register(RespMaterial)