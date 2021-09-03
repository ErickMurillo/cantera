from django.contrib import admin
from django.db.models.base import Model
from .models import *

# Register your models here.
# class FotosCompromisos_Inline(admin.TabularInline):
# 	model = FotosCompromisos
# 	extra = 1
# 	max_num = 4
	
class CompromisoAdmin(admin.ModelAdmin):
	# inlines = [FotosCompromisos_Inline,]
	list_display = ('pais','conteo_hombres','conteo_mujeres')

admin.site.register(Compromiso,CompromisoAdmin)