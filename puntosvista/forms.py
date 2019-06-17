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
		exclude = ('slug', 'usuario',)