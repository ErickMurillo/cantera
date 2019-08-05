from django.contrib import admin
from .models import *

# Register your models here.
class GaleriaInline(admin.TabularInline):
	model = Galeria
	extra = 1

class ActualidadAdmin(admin.ModelAdmin):
	inlines = [GaleriaInline,]

admin.site.register(Actualidad,ActualidadAdmin)
admin.site.register(Temas)

#paginas estaticas
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
 
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
 
class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = FlatPage
        fields = '__all__'
 
 
class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm
 
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)