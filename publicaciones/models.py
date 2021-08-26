from django.db import models
from sorl.thumbnail import ImageField
from users.models import User
from actualidad.models import * 
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from embed_video.fields import EmbedVideoField
from taggit_autosuggest.managers import TaggableManager

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

	def __str__(self):
		return u'%s' % self.titulo

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(Publicacion, self).save(*args, **kwargs)

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