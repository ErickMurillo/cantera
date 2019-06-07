from django.urls import path 
from .views import *

urlpatterns = [
	path('', list_actualidad, name='list_actualidad'),
	path('<category>/', filtro_categoria, name='filtro-categoria'),
	path('tag/<slug>/', filtro_tag, name='filtro-tag'),
	path('detalle/<slug>/', detalle_actualidad, name='detalle-actualidad'),
]