# Generated by Django 5.0.4 on 2024-05-23 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libros', '0003_libro_idioma_libro_paginas_alter_libro_anio'),
        ('usuarios', '0006_remove_usuario_name_remove_usuario_pw_usuario_avatar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAlta', models.DateField(auto_now=True)),
                ('libro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='libros.libro')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
            ],
        ),
    ]
