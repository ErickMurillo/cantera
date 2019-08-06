from django.urls import path
from . import views

urlpatterns = [
	path('',views.index_org, name = 'list_org'),
	path('editar/<id>/', views.org_editar, name = 'org_editar'),
	#actualidad
	path('actualidad/',views.actualidad_list, name ='actualidad_list'),
	path('actualidad/agregar/',views.actualidad_crear, name = 'actualidad_crear'),
	path('actualidad/editar/<id>/', views.actualidad_editar, name = 'actualidad_editar'),
	path('actualidad/eliminar/<id>/',views.eliminar_actualidad, name = 'eliminar_actualidad'),
	#Foros
	path('foros/', views.foros_list, name = 'foros_list'),
	path('foros/agregar/', views.foros_crear, name = 'foros_crear'),
	path('foros/editar/<id>/', views.foros_editar, name = 'foros_editar'),
	path('foros/eliminar/<id>/', views.foro_eliminar, name = 'foro_eliminar'),
	#eventos
	path('iniciativas-destacadas/', views.events_list, name = 'events_list'),
	path('iniciativas-destacadas/eventos/agregar/', views.events_crear, name = 'events_crear'),
	path('iniciativas-destacadas/eventos/eliminar/<id>/', views.events_eliminar, name = 'events_eliminar'),
	path('iniciativas-destacadas/eventos/editar/<id>/', views.events_editar, name = 'events_editar'),
	#Galeria-imagenes	
	path('recursos-metodologicos/', views.recursos_list, name = 'recursos_list'),
	path('recursos-metodologicos/galerias/imagenes/agregar/', views.galeria_img_crear, name = 'galeria_img_crear'),
	path('recursos-metodologicos/galerias/imagenes/editar/<id>/', views.galeria_img_editar, name = 'galeria_img_editar'),
	path('recursos-metodologicos/galerias/imagenes/eliminar/<id>/', views.galeria_img_eliminar, name = 'galeria_img_eliminar'),
	#galeria-videos
	path('recursos-metodologicos/galerias/videos/agregar/', views.galeria_vid_crear, name = 'galeria_vid_crear'),
	path('recursos-metodologicos/galerias/videos/editar/<id>/', views.galeria_vid_editar, name = 'galeria_vid_editar'),
	path('recursos-metodologicos/galerias/videos/eliminar<id>/', views.galeria_vid_eliminar, name = 'galeria_vid_eliminar'),
	#galeria-audios
	path('recursos-metodologicos/galerias/audios/agregar/', views.galeria_audio_crear, name = 'galeria_audio_crear'),
	path('recursos-metodologicos/galerias/audios/editar/<id>/', views.galeria_audio_editar, name = 'galeria_audio_editar'),
	path('recursos-metodologicos/galerias/audios/eliminar<id>/', views.galeria_audio_eliminar, name = 'galeria_audio_eliminar'),
	#publicaciones
	path('recursos-metodologicos/publicaciones/agregar/', views.publicacion_agregar, name = 'publicacion_agregar'),
	path('recursos-metodologicos/publicaciones/editar/<id>/', views.publicacion_editar, name = 'publicacion_editar'),
	path('recursos-metodologicos/publicaciones/eliminar/<id>/', views.publicacion_eliminar, name = 'publicacion_eliminar'),
	#guias
	path('recursos-metodologicos/guias/agregar/', views.guia_agregar, name = 'guias_agregar'),
	path('recursos-metodologicos/guias/editar/<id>/', views.publicacion_editar, name = 'guias_editar'),
	path('recursos-metodologicos/guias/eliminar/<id>/', views.publicacion_eliminar, name = 'guias_eliminar'),
	#puntos de vista
	path('puntos-vista/',views.puntos_vista_list, name = 'puntos-vista'),
	path('puntos-vista/agregar/',views.puntos_vista_crear, name = 'puntos_vista_crear'),
	path('puntos-vista/editar/<slug>/',views.puntos_vista_edit, name = 'puntos_vista_edit'),
	path('puntos-vista/eliminar/<id>/',views.puntos_vista_eliminar, name = 'puntos_vista_eliminar'),
	#campania
	path('campanias/agregar/',views.campanias_crear, name = 'campanias_crear'),
	path('campanias/editar/<id>/', views.campanias_editar, name = 'campanias_editar'),
	path('campanias/eliminar/<id>/',views.eliminar_campania, name = 'eliminar_campania'),
	#concursos
	path('concursos/agregar/',views.concursos_crear, name = 'concursos_crear'),
	path('concursos/editar/<id>/', views.concursos_editar, name = 'concursos_editar'),
	path('concursos/eliminar/<id>/',views.eliminar_concursos, name = 'eliminar_concursos'),
	
	path('<slug>/', views.detalles_org, name = 'detalles_organizaciones'),

]	