# Generated by Django 5.0.4 on 2024-05-30 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0004_alter_libro_editorial_remove_autor_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='libros.autor'),
        ),
    ]
