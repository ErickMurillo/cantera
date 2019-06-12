from django.urls import path
from . import views

urlpatterns = [
	path('eventos/',views.indexEventos, name = 'indexEventos'),
	path('eventos/<slug>/',views.detailEventos, name = 'detailEventos'),
	path('eventos/tag/<slug>',views.filtro_tag_eventos, name ='filtro_tag_eventos'),
	path('campanias/',views.indexCampanias,name = 'indexCampanias'),
	path('campanias/<slug>',views.detailCampanias, name = 'detail_campanias'),
	path('campanias/tag/<slug>/',views.filtro_tag_campanias, name='filtro-tag-camp'),
	path('concursos/',views.indexConcursos, name = 'indexConcursos'),
	path('concursos/<slug>', views.detailConcursos, name = 'detailConcursos'),
	path('concurso/tag/<slug>/',views.filtro_tag_concurso, name='filtro_tag_concurso'),

]