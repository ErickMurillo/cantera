# Generated by Django 2.1.7 on 2019-05-07 16:01

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actualidad', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aportes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name_plural': 'Aportes',
            },
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('comentario', ckeditor_uploader.fields.RichTextUploadingField()),
                ('aporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foro.Aportes')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Foros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('apertura', models.DateField(verbose_name='Apertura y recepción de aportes')),
                ('cierre', models.DateField(verbose_name='Cierre de aportes')),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(editable=False, max_length=200)),
                ('tematica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actualidad.Temas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Foros',
                'ordering': ['-creacion'],
            },
        ),
        migrations.AddField(
            model_name='aportes',
            name='foro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foro.Foros'),
        ),
        migrations.AddField(
            model_name='aportes',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]