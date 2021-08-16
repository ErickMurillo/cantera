from django.urls import path
from . import views

urlpatterns = [
	path('imagenes/',views.index_galeriasImagenes, name = 'index_galeriasImagenes'),
	path('imagenes/tematica/<tema>/', views.filtro_temas_img, name='filtro_temas_img'),
	path('imagenes/<slug>/',views.detalle_galeriaImagenes, name = 'detalle_galeriaImagenes'),
	path('videos/',views.index_galeriaVideos, name = 'index_galeriaVideos'),
	path('videos/tematica/<tema>/', views.filtro_temas_vid, name='filtro_temas_vid'),
	path('videos/<slug>/',views.detalle_galeria_vid, name = 'detalle_galeria_vid'),
	path('audios/',views.index_galeriaaudio, name = 'index_galeriaaudio'),
	path('audios/tematica/<tema>/', views.filtro_temas_audio, name='filtro_temas_audio'),
	path('audios/<slug>/',views.detalle_galeria_audio, name = 'detalle_galeria_audio'),

]