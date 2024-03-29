from django.urls import path
from . import views

urlpatterns = [
	path('publicaciones/',views.index_publicaciones, name='index_publicaciones'),
	path('publicaciones/<slug>/',views.detail_publicacion, name='detail_publicacion'),
	path('publicaciones/palabras-claves/<tag>/',views.filtro_tags, name='filtro_publicacion_tags'),
	path('busqueda/publicaciones/', views.search_publicacion, name = 'search-publicacion'),
	path('guias-metodologicas/', views.index_guias, name ='index_guias'),
	path('guias-metodologicas/<slug>/', views.detail_guias, name = 'detail_guias'),
]