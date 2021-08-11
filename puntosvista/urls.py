from django.urls import path 
from . import views

urlpatterns = [
	path('',views.list_puntos, name = 'list_puntos'),
	path('<slug>/', views.point_details, name = 'point_details'),
]