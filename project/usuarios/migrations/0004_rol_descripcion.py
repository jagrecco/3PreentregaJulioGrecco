# Generated by Django 5.0.4 on 2024-05-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_pw'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
    ]
