from django.db import models
from users.models import User
from organizaciones.models import *

# Create your models here.

class SolicitudesOrg(models.Model):
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	organizacion = models.ForeignKey(Contraparte,on_delete=models.DO_NOTHING)
	aprobado = models.BooleanField()

	class Meta:
		verbose_name = 'Solicitud para unirse a una organización'
		verbose_name_plural = 'Solicitudes a organizaciones'

class SolicitudesNuevasOrg(models.Model):
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	nombre_org = models.CharField(max_length=200)
	siglas_org = models.CharField("Siglas o nombre corto",help_text="Siglas o nombre corto de la oganización",max_length=200)
	pais_org = models.ForeignKey(Pais,on_delete=models.DO_NOTHING)
	aprobado = models.BooleanField()

	class Meta:
		verbose_name = 'Solicitud para crear una organización'
		verbose_name_plural = 'Solicitudes nuevas organizaciones'