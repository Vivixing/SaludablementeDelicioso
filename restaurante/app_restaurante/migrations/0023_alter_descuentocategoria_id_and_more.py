# Generated by Django 4.2 on 2023-05-22 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurante', '0022_alter_descuentocumple_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuentocategoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='descuentoproducto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
