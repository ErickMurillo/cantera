from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from location_field.models.plain import PlainLocationField
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
	tittle = models.CharField('Título',max_length=200)
	foto = ImageField('Foto',upload_to='eventos/')
	descripcion = RichTextUploadingField()
	inicio = models.DateField('Fecha de Inicio')
	final = models.DateField('Fecha de Finalización',null=True, blank=True)
	hora_inicio = models.TimeField('Hora inicio')
	hora_fin = models.TimeField('Hora fin')
	city = models.CharField('Dirección', max_length=100)
	position = PlainLocationField(based_fields=['city'], zoom=7,verbose_name='Posición')
	slug = models.SlugField(max_length=200, editable=False)
	author = models.ForeignKey(User,on_delete=models.DO_NOTHING)

	class Meta:
		verbose_name_plural = 'Eventos'

	def __str__(self):
		return self.tittle

	def save(self,*args,**kwargs):
		self.slug = slugify(self.tittle)
		return super(Evento,self).save(*args,*kwargs)
