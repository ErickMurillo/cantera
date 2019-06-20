# -*- coding: UTF-8 -*-
from django.db import models
from django.forms import ModelForm
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import User
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, SelectDateWidget

class ContraparteForms(forms.ModelForm):
	temas = forms.CharField(widget=CKEditorUploadingWidget())
	siglas = forms.CharField(widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Siglas o nombre corto"}))
	generalidades = forms.CharField(widget=CKEditorUploadingWidget())
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'span7','rel':"tooltip", 'title':"Nombre completo de la contraparte"}))
	fundacion = forms.CharField(widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Año en que fue fundada la organización"}))
	contacto = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Nombre completo de la persona de contacto"}))
	correo = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Correo de la persona de contacto"}))
	telefono = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Formato ### - ######## "}))

	class Meta:
		model = Contraparte
		fields = '__all__'

class RedesFrom(forms.ModelForm):
	class Meta:
		model = Redes
		fields = '__all__'
		exclude = ['organizacion',]
