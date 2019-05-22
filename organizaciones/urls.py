from django.urls import path
from . import views

urlpatterns = [
	path('',views.index_org, name = 'list_org'),
	path('actualidad/',views.actualidad_list, name ='actualidad_list'),
	path('actualidad/agregar',views.actualidad_crear, name = 'actualidad_crear'),
	path('actualidad/<slug>/editar/', views.actualidad_editar, name = 'actualidad_editar'),
	path('foros/', views.foros_list, name = 'foros_list'),
	path('foros/agregar', views.foros_crear, name = 'foros_crear'),
	path('iniciativas-destacadas/eventos/', views.events_list, name = 'iniciativas_list'),
	path('recursos-metodologicos/galerias/', views.galeria_list, name = 'galeria_list'),
	path('recursos-metodologicos/galerias/imagenes/agregar', views.galeria_img_crear, name = 'galeria_img_crear'),
	path('recursos-metodologicos/galerias/videos/agregar', views.galeria_vid_crear, name = 'galeria_vid_crears'),
	path('<slug>/', views.detalles_org, name = 'detalles_organizaciones'),

]	