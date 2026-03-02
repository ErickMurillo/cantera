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

class PreguntasForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['utilizara_material'] = forms.ChoiceField(choices=UTIL_CHOICES)
		self.fields['perfil'] = forms.ChoiceField(choices=PERFIL_CHOICES)