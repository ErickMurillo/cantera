from django.db import models
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField

class EventsForms(forms.ModelForm):
	descripcion = forms.CharField(widget=CKEditorUploadingWidget())

	class Meta:
		model = Evento
		fields = '__all__'
		exclude = ('slug', 'author','aprobado')
		help_texts = {
			'foto': 'Tamaño de imagen recomendado: 830x620',
		}

class GaleriaEventosForm(forms.ModelForm):
	class Meta:
		model = GaleriaEventos
		fields = '__all__'