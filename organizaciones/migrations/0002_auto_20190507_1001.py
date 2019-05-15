# Generated by Django 2.1.7 on 2019-05-07 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', sorl.thumbnail.fields.ImageField(upload_to='usuario/avatar/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Avatar usuario',
                'verbose_name_plural': 'Avatars usuarios',
            },
        ),
        migrations.AddField(
            model_name='contraparte',
            name='usuarios',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]