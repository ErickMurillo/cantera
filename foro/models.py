from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from sorl.thumbnail import ImageField
from users.models import User
from actualidad.models import *

# Create your models here.
class Foros(models.Model):
	nombre = models.CharField(max_length=200, unique=True)
	creacion = models.DateField('Fecha de creación')
	apertura = models.DateField('Apertura y recepción de aportes')
	cierre = models.DateField('Cierre de aportes')
	foto = ImageField('Foto',upload_to='foros/')
	contenido = RichTextUploadingField()
	tematica = models.ForeignKey(Temas,on_delete=models.DO_NOTHING)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	slug = models.SlugField(max_length=200,editable=False)

	class Meta:
		verbose_name_plural = "Foros"
		ordering = ['-creacion']

	def __str__(self):
		return self.nombre

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
		return self.foro.nombre

class Comentarios(models.Model):
	fecha = models.DateField(auto_now_add=True)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	comentario = RichTextUploadingField()
	aporte = models.ForeignKey(Aportes,on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Comentarios"

	def __str__(self):
		return self.usuario.username
