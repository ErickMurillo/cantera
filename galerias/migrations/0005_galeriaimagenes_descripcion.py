# Generated by Django 2.1.7 on 2019-08-20 21:18

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galerias', '0004_auto_20190806_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeriaimagenes',
            name='descripcion',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='descripcion'),
            preserve_default=False,
        ),
    ]
