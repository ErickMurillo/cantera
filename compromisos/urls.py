from django.urls import path 
from .views import *

urlpatterns = [
    path('get-json/', get_compromisos, name='get-compromisos'),
    path('get-json/detalle/', get_compromisos_detalle, name='get-compromisos-detalle'),
]