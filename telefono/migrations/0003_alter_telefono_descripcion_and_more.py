# Generated by Django 4.2.6 on 2023-11-14 22:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telefono', '0002_alter_telefono_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='fecha_creacion',
            field=models.DateField(),
        ),
    ]