from django.db import models
from solo.models import SingletonModel
from sorl.thumbnail import ImageField

# Create your models here.

class SiteConfiguration(SingletonModel):
	foto_actualidad = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_eventos = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_galerias_videos = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_galerias_imagenes = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_foros = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_puntos_vista = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_quienes_somos = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_guias_metodologicas = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_publicaciones = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_campanias = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_concursos = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')
	foto_alianzas = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1350x230')

	def __unicode__(self):
		return "Configuracion imagenes del sitio"

	class Meta:
		verbose_name_plural = "Configuracion imagenes del sitio"

class Slider(SingletonModel):
	texto_1 = models.CharField(max_length=60,verbose_name='Texto')
	foto_1 = ImageField('Foto',upload_to='slider/')
	credito_1 = models.CharField(max_length=100,verbose_name='Credito')

	texto_2 = models.CharField(max_length=60,blank=True,null=True,verbose_name='Texto')
	foto_2 = ImageField('Foto',upload_to='slider/',blank=True,null=True)
	credito_2 = models.CharField(max_length=100,blank=True,null=True,verbose_name='Credito')

	texto_3 = models.CharField(max_length=60,blank=True,null=True,verbose_name='Texto')
	foto_3 = ImageField('Foto',upload_to='slider/',blank=True,null=True)
	credito_3 = models.CharField(max_length=100,blank=True,null=True,verbose_name='Credito')

	def __unicode__(self):
		return u"Slider"

	class Meta:
		verbose_name_plural = "Slider inicio"
