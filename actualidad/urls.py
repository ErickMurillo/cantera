from django.urls import path 
from . import views

urlpatterns = [
	path('',views.list_actualidad, name='list_actualidad'),
	path('<slug>/',views.detalle_actualidad, name='detalle_actualidad'),
]