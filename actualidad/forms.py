from django.db import models
from .models import *
from django import forms

class Actualidad(forms.ModelForm):
	class Meta:
		model: Actualidad
		
			