# Generated by Django 5.2.3 on 2025-06-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_remove_usuario_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='perfiles/'),
        ),
    ]
