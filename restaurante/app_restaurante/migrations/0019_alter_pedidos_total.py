# Generated by Django 4.2 on 2023-05-22 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurante', '0018_alter_pedidos_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='total',
            field=models.DecimalField(decimal_places=0, editable=False, max_digits=10),
        ),
    ]
