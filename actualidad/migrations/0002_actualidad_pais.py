# Generated by Django 2.1.7 on 2019-07-23 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0002_auto_20190624_1011'),
        ('actualidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualidad',
            name='pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='organizaciones.Pais'),
            preserve_default=False,
        ),
    ]
