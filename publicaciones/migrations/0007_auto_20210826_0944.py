# Generated by Django 2.1.7 on 2021-08-26 09:44

from django.db import migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('publicaciones', '0006_publicacion_palabras_claves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='palabras_claves',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Separar elementos con "," ', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Palabras claves'),
        ),
    ]
