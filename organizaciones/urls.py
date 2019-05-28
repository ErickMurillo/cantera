from django.urls import path
from . import views

urlpatterns = [
	path('',views.index_org, name = 'list_org'),
	path('<id>/editar/', views.org_editar, name = 'org_editar'),
	#actualidad
	path('actualidad/',views.actualidad_list, name ='actualidad_list'),
	path('actualidad/agregar/',views.actualidad_crear, name = 'actualidad_crear'),
	path('actualidad/<id>/editar/', views.actualidad_editar, name = 'actualidad_editar'),
	path('actualidad/<id>/eliminar/',views.eliminar_actualidad, name = 'eliminar_actualidad'),
	#Foros
	path('foros/', views.foros_list, name = 'foros_list'),
	path('foros/agregar', views.foros_crear, name = 'foros_crear'),
	#eventos
	path('iniciativas-destacadas/eventos/editar', views.edit_event, name ='edit_event'),
	path('iniciativas-destacadas/eventos/', views.events_list, name = 'events_list'),
	path('iniciativas-destacadas/eventos/agregar/', views.events_crear, name = 'events_crear'),
	path('iniciativas-destacadas/eventos/<id>/eliminar/', views.events_eliminar, name = 'events_eliminar'),
	path('iniciativas-destacadas/eventos/<id>/editar/', views.events_editar, name = 'events_editar'),
	#Galeria-imagenes	
	path('recursos-metodologicos/galerias/', views.galeria_list, name = 'galeria_list'),
	path('recursos-metodologicos/galerias/imagenes/agregar/', views.galeria_img_crear, name = 'galeria_img_crear'),
	path('recursos-metodologicos/galerias/imagenes/<id>/editar/', views.galeria_img_editar, name = 'galeria_img_editar'),
	path('recursos-metodologicos/galerias/imagenes/<id>/eliminar/', views.galeria_img_eliminar, name = 'galeria_img_eliminar'),
	#galeria-videos
	path('recursos-metodologicos/galerias/videos/agregar/', views.galeria_vid_crear, name = 'galeria_vid_crear'),
	path('recursos-metodologicos/galerias/videos/<id>/editar/', views.galeria_vid_editar, name = 'galeria_vid_editar'),
	path('recursos-metodologicos/galerias/videos/<id>/eliminar', views.galeria_vid_eliminar, name = 'galeria_vid_eliminar'),
	#puntos de vista
	path('puntos-vista/',views.puntos_vista_list, name = 'puntos-vista'),
	path('puntos-vista/agregar/',views.puntos_vista_crear, name = 'puntos_vista_crear'),
	path('puntos-vista/<slug>/editar/',views.puntos_vista_edit, name = 'puntos_vista_edit'),
	path('puntos-vista/<id>/eliminar/',views.puntos_vista_eliminar, name = 'puntos_vista_eliminar'),
	
	path('<slug>/', views.detalles_org, name = 'detalles_organizaciones'),

]	