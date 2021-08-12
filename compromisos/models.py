from django.db import models
from sorl.thumbnail import ImageField
from . import dataCountries as data

# Create your models here.
class Compromiso(models.Model):
	pais = models.CharField(max_length=3,choices=data.COUNTRIES_CODE_CHOICES)
	conteo_hombres = models.IntegerField()
	conteo_mujeres = models.IntegerField()
	total = models.IntegerField(editable=False)

	class Meta:
		verbose_name_plural = 'Compromisos'

	def __str__(self):
		return self.pais
	
	def save(self,*args,**kwargs):
		self.total = self.conteo_mujeres + self.conteo_hombres
		return super(Compromiso,self).save(*args,*kwargs)

class FotosCompromisos(models.Model):
	compromiso = models.ForeignKey(Compromiso, on_delete=models.CASCADE)
	foto = ImageField()

	class Meta:
		verbose_name_plural = 'Fotos'
