from django.db import models

# Create your models here.

class Comida_menu(models.Model):  #nombre de la tabla en la Base de Datos
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    descripcion = models.CharField(max_length=300, default='DEFAULT VALUE')
    #stock = models.TextChoices('Si Hay', 'No hay')
    stock = models.CharField(max_length=100, default='DEFAULT VALUE')
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
'''
class Usuario_restaurante(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    apellido = models.CharField(max_length=100, default='DEFAULT VALUE')
    contraseña = models.CharField(max_length=10, default='DEFAULT VALUE')
    email = models.EmailField(max_length=100, default='DEFAULT VALUE')
    usuario = models.CharField(max_length=100, default='DEFAULT VALUE')
''' 

class Meta:
     db_table = 'comida' #nombre de instancia con la que llamamos la tabla en la Base de Datos
    # db_table = 'usuario'