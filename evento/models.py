from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from location_field.models.plain import PlainLocationField
from sorl.thumbnail import ImageField
from users.models import User
from taggit_autosuggest.managers import TaggableManager
from django.urls import reverse

# Create your models here.

class Evento(models.Model):
	tittle = models.CharField('Título',max_length=200, unique=True)
	foto = ImageField('Foto',upload_to='eventos/',help_text = '830x620')
	descripcion = RichTextUploadingField('Descripción')
	inicio = models.DateField('Fecha de Inicio')
	final = models.DateField('Fecha de Finalización',null=True, blank=True)
	hora_inicio = models.TimeField('Hora inicio',null=True, blank=True)
	hora_fin = models.TimeField('Hora fin',null=True, blank=True)
	city = models.CharField('Dirección', max_length=100,null=True,blank=True)
	position = PlainLocationField(based_fields=['city'], zoom=7,verbose_name='Posición',null=True,blank=True)
	slug = models.SlugField(max_length=200, editable=False)
	tags = TaggableManager("Tags",help_text='Separar elementos con "," ', blank=True)
	author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='Autor')
	aprobado = models.BooleanField()

	class Meta:
		verbose_name_plural = 'Eventos'

	def __str__(self):
		return self.tittle
	
	def get_absolute_url(self):
		return reverse('detailEventos',kwargs={'slug': self.slug})

	def save(self,*args,**kwargs):
		self.slug = slugify(self.tittle)
		return super(Evento,self).save(*args,*kwargs)

class GaleriaEventos(models.Model):
	evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=90)
	imagen = ImageField(upload_to='galerias/evento/')
