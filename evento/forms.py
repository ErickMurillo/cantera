from django.db import models
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField

class EventsForms(forms.ModelForm):
	descripcion = forms.CharField(widget=CKEditorUploadingWidget())
	#foto = forms.ImageField(required=True)
	#tittle = forms.CharField(widget=forms.TextInput(attrs={'class':'span7','rel':"tooltip", 'title':"Tratar de redactar títulos resumidos"}))

	class Meta:
		model = Evento
		fields = '__all__'
		exclude = ('slug', 'author',)