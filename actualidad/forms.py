from django.db import models
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField

Types_actualidad = (
	(1,'Informémonos'),
	(2,'Situación regional de género'),
	(3,'Reflexiones')
)

class ActualidadForms(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	photo = forms.ImageField(required=True)
	category = forms.ChoiceField(choices = Types_actualidad)
	tittle = forms.CharField(widget=forms.TextInput(attrs={'class':'span7','rel':"tooltip", 'title':"Tratar de redactar títulos resumidos"}))
	class Meta:
		model = Actualidad
		fields = '__all__'
		exclude = ('slug','created_on','author',)
			