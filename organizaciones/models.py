from django.db import models
from sorl.thumbnail import ImageField
# from users.models import User
from actualidad.models import * 
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,editable=False)

    class Meta:
        verbose_name_plural = "Países"

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        return super(Pais, self).save(*args, **kwargs)

class Contraparte(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField("Siglas o nombre corto",help_text="Siglas o nombre corto de la oganización",max_length=200)
    logo = ImageField(upload_to='contrapartes/logos/',null=True, blank=True,help_text='240x170')
    pais = models.ForeignKey(Pais,on_delete=models.DO_NOTHING)
    fundacion = models.CharField('Año de fundación', max_length=200,blank=True, null=True)
    temas = RichTextUploadingField(blank=True, null=True)
    generalidades = RichTextUploadingField(blank=True, null=True)
    contacto = models.CharField(max_length=200,blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    # usuarios = models.ManyToManyField(User,blank=True)
    slug = models.SlugField(max_length=200,editable=False)

    class Meta:
        verbose_name_plural = "Alianzas"

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        return super(Contraparte, self).save(*args, **kwargs)
        
REDES_CHOICES = (('Sitio web','Sitio web'),('Facebook','Facebook'),('Twitter','Twitter'),('Youtube','Youtube'),
					('Instagram','Instagram'),('Linkedin','Linkedin'),
					('Flickr','Flickr'),('Pinterest','Pinterest'),('Vimeo','Vimeo'),('Otra','Otra'),)

class Redes(models.Model):
	organizacion = models.ForeignKey(Contraparte,on_delete=models.DO_NOTHING)
	opcion = models.CharField(max_length=25,choices=REDES_CHOICES)
	url = models.URLField()

	class Meta:
		verbose_name = 'Red'
		verbose_name_plural = 'Redes'
