# Generated by Django 4.2 on 2023-05-21 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurante', '0013_alter_pedidos_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='total',
            field=models.PositiveIntegerField(),
        ),
    ]
