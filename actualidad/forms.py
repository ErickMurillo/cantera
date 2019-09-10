from django.db import models
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from embed_video.fields import EmbedVideoField
# from sorl.thumbnail import ImageField

Types_actualidad = (
	('noticias','Noticias'),
	('situacion-regional-genero','Situación regional de género'),
)

class GaleriaForm(forms.ModelForm):
	class Meta:
		model = Galeria
		fields = '__all__'

class ActualidadForms(forms.ModelForm):
	content = forms.CharField(label='Contenido',widget=CKEditorUploadingWidget())
	# category = forms.ChoiceField(label='Categoría',choices = Types_actualidad)
	
	class Meta:
		model = Actualidad
		fields = '__all__'
		exclude = ('slug','created_on','author','category','aprobado')
		help_texts = {
			'photo': 'Tamaño de imagen recomendado: 830x620',
		}

class Actualidad2Forms(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	
	class Meta:
		model = Actualidad
		fields = '__all__'
		exclude = ('slug','created_on','author','category','aprobado')
		help_texts = {
			'photo': 'Tamaño de imagen recomendado: 830x620',
		}

class BuscadorGeneral(forms.Form):
	q = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'type': 'text',
			'id': 'widget-search',
			'placeholder': 'Buscar...',
			'name': 'search',
		}))
			