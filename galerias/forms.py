# -*- coding: utf-8 -*-
from django.db import models
from .models import *
from django import forms

class GaleriaImagenesForm(forms.ModelForm):
	class Meta:
		model = GaleriaImagenes
		exclude = ('usuario','slug','aprobado')
		help_texts = {
			'portada': 'Tamaño de imagen recomendado: 830x620',
		}

class ImagenesForm(forms.ModelForm):
	class Meta:
		model = Imagenes
		fields = '__all__'
		help_texts = {
			'imagen': 'Tamaño de imagen recomendado: 830x620',
		}

class GaleriaVideosForm(forms.ModelForm):
	class Meta:
		model = GaleriaVideos
		exclude = ('usuario','slug','aprobado')
		help_texts = {
			'portada': 'Tamaño de imagen recomendado: 830x620',
		}

class ListVideosForm(forms.ModelForm):
	class Meta:
		model = ListVideos
		fields = '__all__'

class AudiosForm(forms.ModelForm):
	class Meta:
		model = Audios
		exclude = ('usuario','slug','aprobado')

class ListAudiosForm(forms.ModelForm):
	class Meta:
		model = ListAudios
		fields = '__all__'