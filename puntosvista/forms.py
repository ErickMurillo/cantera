from django.db import models
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from sorl.thumbnail import ImageField

class PuntosForms(forms.ModelForm):
	contenido = forms.CharField(widget=CKEditorUploadingWidget())
	
	class Meta:
		model = Puntos
		fields = '__all__'
		exclude = ('slug', 'usuario','aprobado')
		help_texts = {
			'foto': 'Tamaño de imagen recomendado: 830x620',
		}

class GaleriaPuntosForm(forms.ModelForm):
	class Meta:
		model = GaleriaPuntos
		fields = '__all__'