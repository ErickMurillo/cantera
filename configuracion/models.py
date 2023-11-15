from django.db import models
from solo.models import SingletonModel
from sorl.thumbnail import ImageField
from colorfield.fields import ColorField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class SiteConfiguration(SingletonModel):
	foto_actualidad = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_eventos = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_galerias_imagenes = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_galerias_videos = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_galerias_audios = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_foros = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_puntos_vista = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_quienes_somos = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_guias_metodologicas = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_publicaciones = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_campanias = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_concursos = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')
	foto_alianzas = ImageField(upload_to='configuracion/',blank=True,null=True,help_text='1400x300')

	def __unicode__(self):
		return "Configuracion imagenes del sitio"

	class Meta:
		verbose_name = "Configuracion imagenes del sitio"

class Slider(SingletonModel):
	texto_1 = models.CharField(max_length=60,verbose_name='Texto',blank=True,null=True)
	color_texto_1 = ColorField(blank=True,null=True)
	foto_1 = ImageField('Foto',upload_to='slider/',help_text='1400x300')
	credito_1 = models.CharField(max_length=100,verbose_name='Credito',blank=True,null=True)

	texto_2 = models.CharField(max_length=60,blank=True,null=True,verbose_name='Texto')
	color_texto_2 = ColorField(blank=True,null=True)
	foto_2 = ImageField('Foto',upload_to='slider/',blank=True,null=True,help_text='1400x300')
	credito_2 = models.CharField(max_length=100,blank=True,null=True,verbose_name='Credito')

	texto_3 = models.CharField(max_length=60,blank=True,null=True,verbose_name='Texto')
	color_texto_3 = ColorField(blank=True,null=True)
	foto_3 = ImageField('Foto',upload_to='slider/',blank=True,null=True,help_text='1400x300')
	credito_3 = models.CharField(max_length=100,blank=True,null=True,verbose_name='Credito')

	def __unicode__(self):
		return u"Slider"

	class Meta:
		verbose_name = "Slider inicio"

TARGET_CHOICES = ((1,'Interna'),(2,'Externa'))

class InformacionDestacada(SingletonModel):
	imagen = ImageField('Foto',upload_to='destacado/',help_text = 'Formatos compatibles: gif, jpge, png. Tamaño: 300x224')
	titulo = models.CharField(max_length=250)
	link = models.URLField()
	navegacion = models.IntegerField(choices = TARGET_CHOICES)
	activo = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Información destacada'

class InformacionIndex(SingletonModel):
	titulo = models.CharField('Título',max_length=200)
	contenido = RichTextUploadingField()
	activo = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Información Index'

class InformacionAlianzas(SingletonModel):
	titulo = models.CharField('Título',max_length=200)
	contenido = RichTextUploadingField()
	activo = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Información Alianzas'

REDES_CHOICES = (('chrome','Sitio web'),('facebook','Facebook'),('twitter','Twitter'),('youtube','Youtube'),
					('instagram','Instagram'),('linkedin','Linkedin'),
					('flickr','Flickr'),('pinterest','Pinterest'),('vimeo','Vimeo'),('otra','Otra'),)

class Redes(models.Model):
	opcion = models.CharField(max_length=25,choices=REDES_CHOICES)
	url = models.URLField()
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.get_opcion_display()

	class Meta:
		verbose_name = 'Red'
		verbose_name_plural = 'Redes'
