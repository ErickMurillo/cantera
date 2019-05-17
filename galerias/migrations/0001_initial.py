# Generated by Django 2.1.7 on 2019-05-17 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actualidad', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GaleriaImagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('portada', sorl.thumbnail.fields.ImageField(upload_to='galerias/')),
                ('slug', models.SlugField(editable=False, max_length=200)),
                ('tematica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actualidad.Temas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Galería imagenes',
                'verbose_name_plural': 'Galerías imagenes',
            },
        ),
        migrations.CreateModel(
            name='GaleriaVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('url', embed_video.fields.EmbedVideoField()),
                ('slug', models.SlugField(editable=False, max_length=200)),
                ('tematica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actualidad.Temas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Galería videos',
                'verbose_name_plural': 'Galerías videos',
            },
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
                ('imagen', sorl.thumbnail.fields.ImageField(upload_to='galerias/')),
                ('imagenes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galerias.GaleriaImagenes')),
            ],
        ),
    ]
