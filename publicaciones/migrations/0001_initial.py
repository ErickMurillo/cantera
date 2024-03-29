# Generated by Django 2.1.7 on 2019-06-21 15:11

import ckeditor_uploader.fields
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
            name='ArchivosPublicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('archivo_pdf', models.FileField(upload_to='publicaciones/archivos/')),
            ],
            options={
                'verbose_name_plural': 'Archivos',
            },
        ),
        migrations.CreateModel(
            name='AudiosPublicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('archivo_audio', models.FileField(upload_to='publicaciones/audios/')),
            ],
            options={
                'verbose_name_plural': 'Audios',
            },
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('imagen', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='publicaciones/img/')),
                ('resumen', ckeditor_uploader.fields.RichTextUploadingField()),
                ('tipo', models.IntegerField(choices=[(1, 'Publicaciones'), (2, 'Guías metodológicas')])),
                ('slug', models.SlugField(editable=False, max_length=250)),
                ('tematica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actualidad.Temas')),
                ('usuario', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Publicaciones',
            },
        ),
        migrations.CreateModel(
            name='VideosPublicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('url', embed_video.fields.EmbedVideoField()),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.Publicacion')),
            ],
            options={
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.AddField(
            model_name='audiospublicacion',
            name='publicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.Publicacion'),
        ),
        migrations.AddField(
            model_name='archivospublicacion',
            name='publicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.Publicacion'),
        ),
    ]
