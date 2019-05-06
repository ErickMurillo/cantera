from django.contrib import admin
from .models import *

# Register your models here.

class RedesInline(admin.TabularInline):
	model = Redes
	extra = 1

class ContraparteAdmin(admin.ModelAdmin):
	inlines = [RedesInline,]

admin.site.register(Pais)
admin.site.register(Contraparte, ContraparteAdmin)
