# Generated by Django 2.1.7 on 2019-08-06 16:38

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('galerias', '0002_auto_20190805_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeriaimagenes',
            name='aprobado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeriavideos',
            name='aprobado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeriavideos',
            name='descripcion',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeriavideos',
            name='portada',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='galerias/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='galeriaimagenes',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='galeriavideos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]