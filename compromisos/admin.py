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

	class Media:
		js = ('https://code.jquery.com/jquery-1.12.4.min.js','https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js','js/admin.js')    
		css = {'all': ('https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css',)}

admin.site.register(Compromiso,CompromisoAdmin)