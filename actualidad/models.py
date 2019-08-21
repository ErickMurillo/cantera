from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from sorl.thumbnail import ImageField
from users.models import User
from taggit_autosuggest.managers import TaggableManager
from organizaciones.models import Pais

# Create your models here.

class Temas(models.Model):
	nombre = models.CharField(max_length=250)

	class Meta: 
		verbose_name_plural = 'Temas'
		verbose_name = 'Tema'

	def __str__(self):
		return self.nombre

Types_actualidad = (
	('noticias','Noticias'),
	('situacion-regional-genero','Situación regional de género'),
	('campanas','Campañas'),
	('concursos','Concursos')
)

class Actualidad(models.Model):
	tittle = models.CharField('Título',max_length=200, unique=True)
	category = models.CharField('Categoría',choices=Types_actualidad, max_length=50)
	pais = models.ForeignKey(Pais,on_delete = models.DO_NOTHING)
	photo = ImageField('Foto',upload_to='actualidad/')
	content = RichTextUploadingField(verbose_name='Contenido')
	created_on = models.DateField('Fecha de publicación', auto_now_add=True)
	tematica = models.ManyToManyField(Temas)
	tags = TaggableManager("Tags",help_text='Separar elementos con "," ', blank=True)
	slug = models.SlugField(max_length=200, editable=False)
	author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='Autor')
	aprobado = models.BooleanField()

	class Meta:
		verbose_name = 'Actualidad'
		verbose_name_plural = "Actualidades"
		ordering = "-created_on", "-id"

	def __str__(self):
		return self.tittle

	def save(self,*args,**kwargs):
		self.slug = slugify(self.tittle)
		return super(Actualidad,self).save(*args,*kwargs)

class Galeria(models.Model):
	actualidad = models.ForeignKey(Actualidad,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=90)
	imagen = ImageField(upload_to='galerias/actualidad/')
			

		