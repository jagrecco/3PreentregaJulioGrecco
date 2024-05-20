# Generated by Django 5.0.4 on 2024-05-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_editorial_genero_remove_libro_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='idioma',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='paginas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='libro',
            name='anio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
