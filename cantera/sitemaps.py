from actualidad.models import Actualidad
from puntosvista.models import Puntos
# from publicaciones.models import Publicacion
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

sitemaps = {
    'noticias': NoticiaSitemap,
    'situacion-regional-genero': SituacionRegionalSitemap,
    'campanias': CampanasSitemap,
    'concursos': ConcursosSitemap,
    'puntos-vista': PuntosSitemap,
}