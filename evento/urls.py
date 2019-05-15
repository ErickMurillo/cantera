from django.urls import path
from . import views

urlpatterns = [
	path('',views.indexEventos, name='indexEventos'),
	path('<slug>/',views.detailEventos, name='detailEventos'),
]