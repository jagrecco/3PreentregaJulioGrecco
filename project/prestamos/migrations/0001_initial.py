# Generated by Django 5.0.4 on 2024-04-29 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libros', '0003_rename_titulo_libro_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAlta', models.DateField(auto_now=True)),
                ('libro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libros.libro')),
            ],
        ),
    ]
