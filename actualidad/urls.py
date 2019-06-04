from django.urls import path 
from . import views

urlpatterns = [
	path('',views.list_actualidad, name='list_actualidad'),
	path('<category>/',views.filtro_categoria, name='filtro-categoria'),
	path('tag/<slug>/',views.filtro_tag, name='filtro-tag'),
	path('<slug>/',views.detalle_actualidad, name='detalle_actualidad'),
]