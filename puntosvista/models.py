from django.db import models
from sorl.thumbnail import ImageField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from users.models import User


# Create your models here.
class Puntos(models.Model):
	tittle = models.CharField('Título',max_length=200, unique=True)
	foto = ImageField('Foto',upload_to='puntos-vista/',help_text = '830x620')
	fecha_creacion = models.DateField('Fecha de publicación',auto_now_add=True)
	contenido =  RichTextUploadingField()
	usuario =  models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='Autor')
	slug = models.SlugField(max_length=200, editable=False)
	aprobado = models.BooleanField()

	class Meta:
		verbose_name_plural = 'Puntos'

	def __str__(self):
		return self.tittle

	def save(self,*args,**kwargs):
		self.slug = slugify(self.tittle)
		return super(Puntos,self).save(*args,*kwargs)

class GaleriaPuntos(models.Model):
	punto = models.ForeignKey(Puntos,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=90)
	imagen = ImageField(upload_to='galerias/puntos/')