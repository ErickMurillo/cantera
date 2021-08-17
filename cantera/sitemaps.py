from actualidad.models import Actualidad
from puntosvista.models import Puntos
from galerias.models import *
from django.contrib.sitemaps import Sitemap, views

class NoticiaSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Actualidad.objects.filter(category = 'noticias',aprobado = True)

    def lastmod(self, obj):
        return obj.created_on

class SituacionRegionalSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Actualidad.objects.filter(category = 'situacion-regional-genero',aprobado = True)

    def lastmod(self, obj):
        return obj.created_on

class CampanasSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Actualidad.objects.filter(category = 'campanas',aprobado = True)

    def lastmod(self, obj):
        return obj.created_on

class ConcursosSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Actualidad.objects.filter(category = 'concursos',aprobado = True)

    def lastmod(self, obj):
        return obj.created_on

class PuntosSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Puntos.objects.filter(aprobado = True)

    def lastmod(self, obj):
        return obj.fecha_creacion
    
class GaleriaImagenesSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return GaleriaImagenes.objects.filter(aprobado = True)

class GaleriaVideosSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return GaleriaVideos.objects.filter(aprobado = True)

class AudiosSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Audios.objects.filter(aprobado = True)

sitemaps = {
    'noticias': NoticiaSitemap,
    'situacion-regional-genero': SituacionRegionalSitemap,
    'campanias': CampanasSitemap,
    'concursos': ConcursosSitemap,
    'puntos-vista': PuntosSitemap,
    'galerias-imagenes': GaleriaImagenesSitemap,
    'galerias-videos': GaleriaVideosSitemap,
    'galerias-audios': AudiosSitemap,
}