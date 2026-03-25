# -*- coding: UTF-8 -*-
from django.db import models
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PublicacionForm(forms.ModelForm):
	resumen = forms.CharField(widget=CKEditorUploadingWidget())

	class Meta:
		model = Publicacion
		exclude = ('slug','usuario','tipo','aprobado')

class ArchivosPublicacionForm(forms.ModelForm):
	class Meta:
		model = ArchivosPublicacion
		fields = '__all__'
		exclude = ['publicacion',]

class AudiosPublicacionForm(forms.ModelForm):
	class Meta:
		model = AudiosPublicacion
		fields = '__all__'
		exclude = ['publicacion',]

class VideosPublicacionForm(forms.ModelForm):
	class Meta:
		model = VideosPublicacion
		fields = '__all__'
		exclude = ['publicacion',]

PERFIL_CHOICES_FORM = (('','---'),(1,'Educador/a o facilitador/a'),(2,'Multiplicador/a comunitario/a'),(3,'Estudiante'),(4,'Integrante de organización social'),
				  (5,'Investigador/a o académico/a'),(6,'Funcionaria/o público'),(7,'Integrante de ONG o cooperación internacional'),
				  (8,'Consultor/a o profesional independiente'),(9,'Persona interesada en temas de género'))

class PreguntasForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['utilizara_material'] = forms.ModelMultipleChoiceField(queryset=RespMaterial.objects.all(),widget=forms.CheckboxSelectMultiple,label="¿Para qué utilizará este material? (Puede seleccionar una o más opciones)")
		self.fields['perfil'] = forms.ChoiceField(choices=PERFIL_CHOICES_FORM,label='¿Cuál es su perfil?')