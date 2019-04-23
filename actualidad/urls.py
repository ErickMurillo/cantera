from django.urls import path 
from . import views

urlpatterns = [
	path('',views.index, name='evento'),
	path('detalle/',views.detail, name='detalle'),
]