# Generated by Django 2.1.7 on 2021-09-13 15:33

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('actualidad', '0004_auto_20190806_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualidad',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(help_text='830x620', upload_to='actualidad/', verbose_name='Foto'),
        ),
    ]
