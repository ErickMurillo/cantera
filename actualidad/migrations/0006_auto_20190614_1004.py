# Generated by Django 2.1.7 on 2019-06-14 16:04

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualidad', '0005_auto_20190611_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualidad',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='actualidad',
            name='created_on',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de publicación'),
        ),
    ]