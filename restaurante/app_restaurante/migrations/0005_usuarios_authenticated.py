# Generated by Django 4.2 on 2023-05-15 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurante', '0004_usuarios_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
