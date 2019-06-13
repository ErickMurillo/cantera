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

class ActualidadForms(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	category = forms.ChoiceField(choices = Types_actualidad)
	
	class Meta:
		model = Actualidad
		fields = '__all__'
		exclude = ('slug','created_on','author',)

class Actualidad2Forms(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	
	class Meta:
		model = Actualidad
		fields = '__all__'
		exclude = ('slug','created_on','author','category')

class BuscadorGeneral(forms.Form):
	q = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'id': 'widget-search',
            'placeholder': 'Buscar...',
            'name': 'search',
        }))
			