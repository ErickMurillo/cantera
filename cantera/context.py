from configuracion.models import *

def imagenes(request):
	foto_eventos = SiteConfiguration.objects.values_list('foto_eventos',flat=True)
	foto_actualidad = SiteConfiguration.objects.values_list('foto_actualidad',flat=True)
	foto_galerias_videos = SiteConfiguration.objects.values_list('foto_galerias_videos',flat=True)
	foto_galerias_imagenes = SiteConfiguration.objects.values_list('foto_galerias_imagenes',flat=True)
	foto_foros = SiteConfiguration.objects.values_list('foto_foros',flat=True)
	foto_puntos_vista = SiteConfiguration.objects.values_list('foto_puntos_vista',flat=True)
	foto_quienes_somos = SiteConfiguration.objects.values_list('foto_quienes_somos',flat=True)

	return {'foto_actualidad':foto_actualidad, 'foto_puntos_vista':foto_puntos_vista,
			'foto_eventos':foto_eventos,'foto_galerias_videos':foto_galerias_videos,
			'foto_galerias_imagenes':foto_galerias_imagenes,'foto_foros':foto_foros,
			'foto_quienes_somos':foto_quienes_somos,
			}