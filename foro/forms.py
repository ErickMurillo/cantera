# -*- coding: UTF-8 -*-

from django.db import models
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class AporteForm(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
    	model = Aportes
    	exclude = ('foro','fecha','usuario',)

class ComentarioForm(forms.ModelForm):
	comentario = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Comentarios
		exclude = ('fecha','usuario',)
		