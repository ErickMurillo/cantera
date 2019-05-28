from django.db import models
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from sorl.thumbnail import ImageField

class PuntosForms(forms.ModelForm):
	contenido = forms.CharField(widget=CKEditorUploadingWidget())
	#foto = forms.ImageField(required=True)
	#tittle = forms.CharField(widget=forms.TextInput(attrs={'class':'span7','rel':"tooltip", 'title':"Tratar de redactar títulos resumidos"}))

	class Meta:
		model = Puntos
		fields = '__all__'
		exclude = ('slug', 'usuario',)