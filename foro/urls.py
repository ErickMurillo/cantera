from django.urls import path
from .views import *

urlpatterns = [
	path('', list_foros, name='foro'),
	path('<slug>/',detail_foro, name='detalle-foro'),
]