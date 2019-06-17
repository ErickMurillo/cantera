from django.urls import path
from .views import *

urlpatterns = [
	path('', list_foros, name='foro'),
	path('<slug>/',detail_foro, name='detalle-foro'),
	path('comentario/agregar/<id>/',add_comentario, name='add_comentario'),
	path('comentario/editar/<id>/', editar_comentario, name='editar_comentario'),
	path('commentario/eliminar/<id>/', eliminar_comentario, name='eliminar_comentario'),
	path('aporte/modificar/<id>/', editar_aporte, name='editar_aporte'),
	path('aporte/eliminar/<id>/', eliminar_aporte, name='eliminar_aporte'),
	path('seguir/<id>/', seguir_foro, name='seguir_foro'),
	path('dejar/seguir/<id>/', dejar_seguir_foro, name='dejar_seguir_foro'),
]