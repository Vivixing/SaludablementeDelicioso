from django.db import models

# Create your models here.

class Comida_menu(models.Model):  #nombre de la tabla en la Base de Datos
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=20,)
    descripcion = models.CharField(max_length=300)
    stock = models.CharField(max_length=100)
    CATEGORIAS = [
        ('Vegetarianos', 'Vegetariano'),
        ('Veganos', 'Vegano'),
        ('Diabéticos', 'Diabetico'),
        ('Bebidas', 'Bebidas'),
        ('Postres', 'Postres'),
    ]
    categoria = models.CharField(max_length=100, choices = CATEGORIAS, default='Vegetarianos')
    img = models.ImageField('Imagen', upload_to='comida', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    usuario = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    nacimiento = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Pedidos(models.Model):
    id = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, to_field='id', db_column='id_usuario', on_delete=models.CASCADE)
    id_comida = models.ForeignKey(Comida_menu, to_field='id', db_column='id_comida', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField(max_length=100, auto_now_add=True)
    
    def total(self):
        return float(self.id_comida.precio) * self.cantidad

    total = models.FloatField(total, blank=True, null=True)

class Meta:
    db_table = 'comida'
    db_table = 'usuarios'
    db_table = 'pedidos'