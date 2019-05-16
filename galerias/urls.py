from django.urls import path
from . import views

urlpatterns = [
	path('imagenes/',views.index_galeriasImagenes, name = 'index_galeriasImagenes'),
	path('imagenes/<slug>/',views.detalle_galeriaImagenes, name = 'detalle_galeriaImagenes'),
]