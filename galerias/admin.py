from django.contrib import admin
from .models import *

# Register your models here.
class ImagenesInline(admin.TabularInline):
	model = Imagenes
	extra = 1

class GaleriaImagenesAdmin(admin.ModelAdmin):
	inlines = [ImagenesInline,]

admin.site.register(GaleriaImagenes)
admin.site.register(GaleriaVideos)