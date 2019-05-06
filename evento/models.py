from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from location_field.models.plain import PlainLocationField

# Create your models here.

class Evento(models.Model):
	"""docstring for Evento"""

	title = models.CharField('Título',max_length=200)
	start_date = models.DateTimeField('Fecha de inicio', auto_now_add=True)
	end_date = models.DateTimeField('Fecha finalización', auto_now_add=True)
	direccion = models.CharField('Dirección',max_length=300)
	name = models.CharField('Ciudad', max_length=100)
    position = PlainLocationField(based_fields=['name'], zoom=7)
    
