# -*- coding: UTF-8 -*-

from django.db import models
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ForoForm(forms.ModelForm):
	contenido = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Foros
		exclude = ('slug','usuario','usuarios_siguiendo','aprobado')
		help_texts = {
			'foto': 'Tamaño de imagen recomendado: 830x620',
		}

class AporteForm(forms.ModelForm):
	contenido = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Aportes
		exclude = ('foro','fecha','usuario',)

class ComentarioForm(forms.ModelForm):
	comentario = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Comentarios
		exclude = ('aporte','fecha','usuario',)
		