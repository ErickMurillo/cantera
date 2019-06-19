# Generated by Django 2.1.7 on 2019-06-19 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foro', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='foros',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='foros',
            name='usuarios_siguiendo',
            field=models.ManyToManyField(blank=True, related_name='siguiendo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='aporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foro.Aportes'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
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
