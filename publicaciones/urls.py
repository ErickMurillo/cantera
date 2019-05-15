from django.urls import path
from . import views

urlpatterns = [
	path('',views.index_publicaciones, name='index_publicaciones'),
	path('<slug>/',views.detail_publicacion, name='detail_publicacion'),
]