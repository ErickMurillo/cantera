from django.urls import path
from . import views

urlpatterns = [
	path('',views.index_org, name = 'list_org'),
	path('actualidad/',views.actualidad_list, name ='actualidad_list'),
	path('foros/', views.foros_list, name = 'foros_list'),
	path('iniciativas-destacadas/eventos/', views.events_list, name = 'iniciativas_list'),
	path('recursos-metodologicos/galerias/imagenes', views.galeria_imagenes_list, name = 'galeria_imagenes_list'),
	path('<slug>/', views.detalles_org, name = 'detalles_organizaciones'),

]	