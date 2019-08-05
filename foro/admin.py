from django.contrib import admin
from .models import *
import nested_admin

class ComentariosInline(nested_admin.NestedStackedInline):
	model = Comentarios
	extra = 1

class AportesInline(nested_admin.NestedStackedInline):
	model = Aportes
	inlines = [ComentariosInline,]
	extra = 1

class ForosAdmin(nested_admin.NestedModelAdmin):
	inlines = [AportesInline,]

admin.site.register(Foros,ForosAdmin)