# Generated by Django 2.1.7 on 2021-08-26 09:44

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('compromisos', '0002_compromiso_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotoscompromisos',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(upload_to='compromisos/'),
        ),
    ]
