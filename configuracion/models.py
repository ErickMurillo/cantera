from django.db import models
from solo.models import SingletonModel
from sorl.thumbnail import ImageField

# Create your models here.

class SiteConfiguration(SingletonModel):
	site_name = models.CharField(max_length=255, default='Nombre del Sitio')

	def __unicode__(self):
		return u"Configuracion del sitio"

	class Meta:
		verbose_name_plural = "Configuracion del sitio"

class Slider(SingletonModel):
	texto_1 = models.CharField(max_length=100,verbose_name='Texto')
	foto_1 = ImageField('Foto',upload_to='slider/')
	credito_1 = models.CharField(max_length=100,verbose_name='Credito')

	texto_2 = models.CharField(max_length=100,blank=True,null=True,verbose_name='Texto')
	foto_2 = ImageField('Foto',upload_to='slider/',blank=True,null=True)
	credito_2 = models.CharField(max_length=100,blank=True,null=True,verbose_name='Credito')

	texto_3 = models.CharField(max_length=100,blank=True,null=True,verbose_name='Texto')
	foto_3 = ImageField('Foto',upload_to='slider/',blank=True,null=True)
	credito_3 = models.CharField(max_length=100,blank=True,null=True,verbose_name='Credito')

	def __unicode__(self):
		return u"Slider"

	class Meta:
		verbose_name_plural = "Slider inicio"
