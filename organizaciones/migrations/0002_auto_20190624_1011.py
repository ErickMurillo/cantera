# Generated by Django 2.1.7 on 2019-06-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contraparte',
            name='siglas',
            field=models.CharField(default=1, help_text='Siglas o nombre corto de la oganización', max_length=200, verbose_name='Siglas o nombre corto'),
            preserve_default=False,
        ),
    ]
