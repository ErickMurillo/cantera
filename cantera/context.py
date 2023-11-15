from configuracion.models import *
from actualidad.forms import *

class BuscadorForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(BuscadorForm, self).__init__(*args, **kwargs)
		self.fields['q'] = forms.CharField()
def imagenes(request):
	foto_eventos = SiteConfiguration.objects.values_list('foto_eventos',flat=True)
	foto_actualidad = SiteConfiguration.objects.values_list('foto_actualidad',flat=True)
	foto_galerias_imagenes = SiteConfiguration.objects.values_list('foto_galerias_imagenes',flat=True)
	foto_galerias_videos = SiteConfiguration.objects.values_list('foto_galerias_videos',flat=True)
	foto_galerias_audios = SiteConfiguration.objects.values_list('foto_galerias_audios',flat=True)
	foto_foros = SiteConfiguration.objects.values_list('foto_foros',flat=True)
	foto_puntos_vista = SiteConfiguration.objects.values_list('foto_puntos_vista',flat=True)
	foto_quienes_somos = SiteConfiguration.objects.values_list('foto_quienes_somos',flat=True)
	foto_guias_metodologicas = SiteConfiguration.objects.values_list('foto_guias_metodologicas',flat=True)
	foto_publicaciones = SiteConfiguration.objects.values_list('foto_publicaciones',flat=True)
	foto_campanias = SiteConfiguration.objects.values_list('foto_campanias',flat=True)
	foto_concursos = SiteConfiguration.objects.values_list('foto_concursos',flat=True)
	foto_alianzas = SiteConfiguration.objects.values_list('foto_alianzas',flat=True)

	search = BuscadorForm()

	redes = Redes.objects.all()

	return {'foto_actualidad':foto_actualidad, 'foto_puntos_vista':foto_puntos_vista,
			'foto_eventos':foto_eventos,'foto_galerias_videos':foto_galerias_videos,
			'foto_galerias_audios':foto_galerias_audios,'foto_foros':foto_foros,
			'foto_quienes_somos':foto_quienes_somos,'foto_guias_metodologicas':foto_guias_metodologicas,
			'foto_publicaciones':foto_publicaciones,'foto_campanias':foto_campanias,
			'foto_concursos':foto_concursos,'foto_alianzas':foto_alianzas,
			'foto_galerias_imagenes':foto_galerias_imagenes,
			'search': search,
			'redes': redes
			}
