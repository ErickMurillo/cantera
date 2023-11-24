from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from sorl.thumbnail import ImageField
from users.models import User
from actualidad.models import *
from django.urls import reverse

from embed_video.fields import EmbedVideoField

# Create your models here.
PORTADA_CHOICES = ((1,'Foto'),(2,'Video'))
class Foros(models.Model):
	nombre = models.CharField(max_length=200, unique=True)
	creacion = models.DateField(auto_now_add=True)
	# apertura = models.DateField('Apertura y recepción de aportes')
	# cierre = models.DateField('Cierre de aportes')

	tipo_portada = models.IntegerField(choices = PORTADA_CHOICES)
	foto = ImageField('Foto',upload_to='foros/',help_text = '830x620')
	url_video = EmbedVideoField(null = True, blank = True)
	contenido = RichTextUploadingField()
	tematica = models.ForeignKey(Temas,on_delete=models.DO_NOTHING)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	usuarios_siguiendo = models.ManyToManyField(User,blank=True,related_name='siguiendo')
	slug = models.SlugField(max_length=200,editable=False)
	aprobado = models.BooleanField()

	class Meta:
		verbose_name_plural = "Foros"
		ordering = ['-creacion']

	def __str__(self):
		return self.nombre
	
	def get_absolute_url(self):
		return reverse('detalle-foro',kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Foros, self).save(*args, **kwargs)

class Aportes(models.Model):
	foro = models.ForeignKey(Foros,on_delete=models.CASCADE)
	fecha = models.DateField(auto_now_add=True)
	contenido = RichTextUploadingField()
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)

	class Meta:
		verbose_name_plural = "Aportes"

	def __str__(self):
		return '%s - %s' % (self.foro.nombre,self.usuario)

class Comentarios(models.Model):
	fecha = models.DateField(auto_now_add=True)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	comentario = RichTextUploadingField()
	aporte = models.ForeignKey(Aportes,on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Comentarios"

	def __str__(self):
		return '%s - %s' % (self.aporte.foro,self.usuario)
