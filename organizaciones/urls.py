from django.urls import path
from . import views

urlpatterns = [
	path('',views.index_org, name = 'list_org'),
	path('<slug>/', views.detalles_org, name = 'detalles_organizaciones'),	

]