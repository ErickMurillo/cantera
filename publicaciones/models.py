from django.db import models
from sorl.thumbnail import ImageField
from users.models import User
from actualidad.models import * 
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from embed_video.fields import EmbedVideoField
from taggit_autosuggest.managers import TaggableManager
from django.urls import reverse
from simple_history.models import HistoricalRecords

# Create your models here.
TIPO_CHOICES = ((1,'Publicaciones'),(2,'Guías metodológicas'))

class Publicacion(models.Model):
	titulo = models.CharField(max_length=250)
	imagen = ImageField(upload_to='publicaciones/img/',null=True, blank=True,help_text=' 612px de ancho')
	resumen = RichTextUploadingField()
	tipo =  models.IntegerField(choices=TIPO_CHOICES,default=1,editable=False)
	tematica = models.ForeignKey(Temas,on_delete=models.DO_NOTHING)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='Autor')
	slug = models.SlugField(max_length=250,editable=False)
	aprobado = models.BooleanField()
	tags = TaggableManager("Palabras claves",help_text='Separar elementos con "," ', blank=True)
	created_on = models.DateField('Fecha de publicación',auto_now_add=True,null=True, blank=True)
	history = HistoricalRecords()

	def __str__(self):
		return u'%s' % self.titulo
	
	def get_absolute_url(self):
		return reverse('detail_publicacion',kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(Publicacion, self).save(*args, **kwargs)
	
	@property
	def fecha_creacion(self):
		return self.history.earliest().history_date


	class Meta:
		verbose_name_plural = 'Publicaciones'

class ArchivosPublicacion(models.Model):
	publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=250)
	archivo_pdf = models.FileField(upload_to='publicaciones/archivos/')

	def __str__(self):
		return u'%s' % self.nombre

	class Meta:
		verbose_name_plural = 'Archivos'

class AudiosPublicacion(models.Model):
	publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=250)
	archivo_audio = models.FileField(upload_to='publicaciones/audios/')

	def __str__(self):
		return u'%s' % self.nombre

	class Meta:
		verbose_name_plural = 'Audios'

class VideosPublicacion(models.Model):
	publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=250)
	url = EmbedVideoField()

	def __str__(self):
		return u'%s' % self.nombre

	class Meta:
		verbose_name_plural = 'Videos'

UTIL_CHOICES = ((1,''),)

PERFIL_CHOICES = ((1,'Educador/a'),(2,'Multiplicador/a'),(3,'Estudiante'),(4,'Organización'),)

class PreguntasPublicacion(models.Model):
	publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
	utilizara_material = models.IntegerField(choices=UTIL_CHOICES,verbose_name='¿Para qué utilizará este material?')
	perfil = models.IntegerField(choices=PERFIL_CHOICES,verbose_name='¿Cuál es su perfil?')