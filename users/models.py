from django.db import models
from django.contrib.auth.models import AbstractUser
from organizaciones.models import *

# Create your models here.
class User(AbstractUser):
	organizacion = models.ForeignKey(Contraparte,on_delete=models.DO_NOTHING,null=True,blank=True)
	avatar = ImageField(upload_to='usuario/avatar/',null=True,blank=True)
	# USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS = []

	def __str__(self):
		return self.username

	class Meta(object):
		unique_together = ('email',)
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'

