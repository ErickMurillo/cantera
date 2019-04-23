from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name='foro'),
	path('detalle/',views.detail, name='detalle'),
]