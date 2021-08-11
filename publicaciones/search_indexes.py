from haystack import indexes
from publicaciones.models import *

class PublicacionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    titulo = indexes.NgramField(model_attr='titulo')
    resumen = indexes.NgramField(model_attr='resumen', null=True)
    tematica = indexes.NgramField(model_attr='tematica', null=True)


    def get_model(self):
        return Publicacion
    
    def prepare_tematica(self, obj):
        return obj.tematica.nombre

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-id')
