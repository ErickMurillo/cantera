# -*- coding: UTF-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from embed_video.fields import EmbedVideoField
from django.template.defaultfilters import slugify
from actualidad.models import *
from ckeditor_uploader.fields import RichTextUploadingField

class GaleriaImagenes(models.Model):
	titulo = models.CharField(max_length=200)
	portada = ImageField(upload_to='galerias/',verbose_name='Imagen')
	tematica = models.ForeignKey(Temas,on_delete=models.DO_NOTHING)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='Autor')
	slug = models.SlugField(max_length=200,editable=False)
	aprobado = models.BooleanField()

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Galería imagenes'
		verbose_name_plural = 'Galerías imagenes'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(GaleriaImagenes, self).save(*args, **kwargs)

class Imagenes(models.Model):
	imagenes = models.ForeignKey(GaleriaImagenes,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=90)
	imagen = ImageField(upload_to='galerias/')

############

class GaleriaVideos(models.Model):
	titulo = models.CharField(max_length=200)
	portada = ImageField(upload_to='galerias/',verbose_name='Imagen',blank=True,null=True)
	descripcion = RichTextUploadingField()
	# url = EmbedVideoField()
	tematica = models.ForeignKey(Temas,on_delete=models.DO_NOTHING)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='Autor')
	slug = models.SlugField(max_length=200,editable=False)
	aprobado = models.BooleanField()

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Galería videos'
		verbose_name_plural = 'Galerías videos'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(GaleriaVideos, self).save(*args, **kwargs)

class ListVideos(models.Model):
	videos = models.ForeignKey(GaleriaVideos,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=90)
	url = EmbedVideoField()

	class Meta:
		verbose_name = 'Video'
		verbose_name_plural = 'Lista videos'

class Audios(models.Model):
	titulo = models.CharField(max_length=200)
	portada = ImageField(upload_to='galerias/',verbose_name='Imagen',blank=True,null=True)
	descripcion = RichTextUploadingField()
	tematica = models.ForeignKey(Temas,on_delete=models.DO_NOTHING)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='Autor')
	slug = models.SlugField(max_length=200,editable=False)
	aprobado = models.BooleanField()

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Galería audios'
		verbose_name_plural = 'Galerías audios'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(Audios, self).save(*args, **kwargs)

class ListAudios(models.Model):
	audios = models.ForeignKey(Audios,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=90)
	archivo = models.FileField(upload_to='audios/')

	class Meta:
		verbose_name = 'Audio'
		verbose_name_plural = 'Lista audios'