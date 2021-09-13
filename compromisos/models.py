from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from . import dataCountries as data

# Create your models here.
class Compromiso(models.Model):
	pais = models.CharField(max_length=3,choices=data.COUNTRIES_CODE_CHOICES,unique = True)
	conteo_hombres = models.IntegerField()
	conteo_mujeres = models.IntegerField()
	total = models.IntegerField(editable=False)
	foto = ImageField(upload_to='compromisos/')

	class Meta:
		verbose_name_plural = 'Compromisos'

	def __str__(self):
		return self.pais
	
	def save(self,*args,**kwargs):
		self.total = self.conteo_mujeres + self.conteo_hombres
		return super(Compromiso,self).save(*args,*kwargs)
	
	@property
	def cached_img(self):
		im = get_thumbnail(self.foto, '300x224', crop='center', quality=99)
		return im.url

# class FotosCompromisos(models.Model):
# 	compromiso = models.ForeignKey(Compromiso, on_delete=models.CASCADE)
# 	foto = ImageField(upload_to='compromisos/')

# 	class Meta:
# 		verbose_name_plural = 'Fotos'
	
# 	@property
# 	def cached_img(self):
# 		im = get_thumbnail(self.foto, '1000', crop='center', quality=99)
# 		return im.url
