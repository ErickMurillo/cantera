"""cantera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

admin.site.site_header = 'Administración Cantera'
admin.site.site_title = 'Cantera'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('contactenos/',contacto),
    path('', TemplateView.as_view(template_name = 'prev_index2.html')),
    path('actualidad/',include('actualidad.urls')),
    path('iniciativas-destacadas/',include('evento.urls')),
    path('foros/',include('foro.urls')),
    path('recursos-metodologicos/galerias/',include('galerias.urls')),
    path('recursos-metodologicos/',include('publicaciones.urls')),
    path('alianzas/',include('organizaciones.urls')),
    #path('organizaciones/', , name = 'organizaciones')
    path('puntos-vista/', include('puntosvista.urls')),
    path('accounts/password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('accounts/signup/', LocaLSignupView.as_view(), name='account_signup'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', perfil, name='perfil'),
    path('accounts/edit/<id>/', editar_perfil, name='editar_perfil'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
