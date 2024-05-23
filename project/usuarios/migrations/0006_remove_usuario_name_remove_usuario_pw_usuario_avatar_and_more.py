# Generated by Django 5.0.4 on 2024-05-22 02:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_persona_mail'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='pw',
        ),
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='mail',
            field=models.EmailField(max_length=250, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]