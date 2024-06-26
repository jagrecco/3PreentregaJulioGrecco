# Generated by Django 5.0.4 on 2024-05-23 22:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_alter_usuario_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='mail',
            field=models.EmailField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.rol'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
