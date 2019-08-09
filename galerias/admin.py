from django.contrib import admin
from .models import *

# Register your models here.
class ImagenesInline(admin.TabularInline):
	model = Imagenes
	extra = 1

class GaleriaImagenesAdmin(admin.ModelAdmin):
	inlines = [ImagenesInline,]

class ListVideosInline(admin.TabularInline):
	model = ListVideos
	extra = 1

class GaleriaVideosAdmin(admin.ModelAdmin):
	inlines = [ListVideosInline]

class ListAudiosInline(admin.TabularInline):
	model = ListAudios
	extra = 1

class AudiosAdmin(admin.ModelAdmin):
	inlines = [ListAudiosInline]

admin.site.register(GaleriaImagenes,GaleriaImagenesAdmin)
admin.site.register(GaleriaVideos,GaleriaVideosAdmin)
admin.site.register(Audios,AudiosAdmin)