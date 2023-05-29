import hashlib
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nombre)
    
class Comida_menu(models.Model):  #nombre de la tabla en la Base de Datos
    nombre = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=300)
    stock = models.CharField(max_length=100)
    #Recoger los datos de la tabla categoria
    categoria = models.ForeignKey(Categoria, to_field='id', db_column='id_categoria', on_delete=models.CASCADE)
    img = models.ImageField('Imagen', upload_to='comida', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  str(self.nombre) + ' '+ str(self.categoria) + '' 



class Usuarios(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    nacimiento = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.usuario.first_name) + ' ' + str(self.usuario.last_name) + ' ' 

    # Autenticar Usuario
    def autenticarUsuario(self, *args, **kwargs):
        auth = Usuarios.objects.filter(nombre=self.usuario.first_name,contraseña=hashlib.md5(self.usuario.password.encode('utf-8')).hexdigest()).exists()
        return auth
    
    # Buscar Usuario
    def buscarUsuario(self, *args, **kwargs):
        aux = Usuarios.objects.filter(nombre=self.usuario.first_name,contraseña=hashlib.md5(self.usuario.password.encode('utf-8')).hexdigest())
        return aux

class Pedidos(models.Model):
    id_usuario = models.ForeignKey(Usuarios, to_field='id', db_column='id_usuario', on_delete=models.CASCADE)
    id_comida = models.ForeignKey(Comida_menu, to_field='id', db_column='id_comida', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField(max_length=100, auto_now_add=True)
    total = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.total = self.id_comida.precio * self.cantidad
        super(Pedidos, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id_usuario) + ' ' + str(self.id_comida) + ' ' + str(self.cantidad) + ' ' + str(self.fecha) + ' ' + str(self.total) + ' '

class DescuentoProducto(models.Model):
    id_comida = models.ForeignKey(Comida_menu, to_field='id', db_column='id_comida', on_delete=models.CASCADE)
    CHOICES = (
        (0.1, 'Descuento 10%'),
        (0.15, 'Descuento 15%'),
        (0.2, 'Descuento 20%'),
        (0.25, 'Descuento 25%'),
        (0.3, 'Descuento 30%'),
        (0.35, 'Descuento 35%'),
        (0.4, 'Descuento 40%'),
        (0.45, 'Descuento 45%'),
        (0.5, 'Descuento 50%'),
    )
    descuento = models.FloatField(choices=CHOICES)
    fecha_inicio = models.DateField(max_length=100)
    fecha_fin = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_comida) + ' ' + str(self.descuento) + ' ' + str(self.fecha_inicio) + ' ' + str(self.fecha_fin) + ' '

class DescuentoCumple(models.Model):
    id_usuario = models.ForeignKey(Usuarios, to_field='id', db_column='id_usuario', on_delete=models.CASCADE)
    descuento = models.FloatField()
    fecha_inicio = models.DateField(max_length=100)
    fecha_fin = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_usuario) + ' ' + str(self.descuento) + ' ' + str(self.fecha_inicio) + ' ' + str(self.fecha_fin) + ' '

class DescuentoCategoria(models.Model):
    id_categoria = models.ForeignKey(Categoria, to_field='id', db_column='id_categoria', on_delete=models.CASCADE)
    CHOICES = (
        (0.1, 'Descuento 10%'),
        (0.15, 'Descuento 15%'),
        (0.2, 'Descuento 20%'),
        (0.25, 'Descuento 25%'),
        (0.3, 'Descuento 30%'),
        (0.35, 'Descuento 35%'),
        (0.4, 'Descuento 40%'),
        (0.45, 'Descuento 45%'),
        (0.5, 'Descuento 50%'),
    )
    descuento = models.FloatField(choices=CHOICES)
    fecha_inicio = models.DateField(max_length=100)
    fecha_fin = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_categoria) + ' ' + str(self.descuento) + ' ' + str(self.fecha_inicio) + ' ' + str(self.fecha_fin) + ' '

class InformacionVenta(models.Model):
    id_comida = models.ForeignKey(Comida_menu, to_field='id', db_column='id_comida', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    totalVenta = models.PositiveIntegerField()
    fecha = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_comida) + ' ' + str(self.cantidad) + ' ' + str(self.totalVenta) + ' ' + str(self.fecha) + ' '

class Delivery(models.Model):
    id_usuario = models.ForeignKey(Usuarios, to_field='id', db_column='id_usuario', on_delete=models.CASCADE)
    id_comida = models.ForeignKey(Comida_menu, to_field='id', db_column='id_comida', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    totalFactura = models.PositiveIntegerField()
    direccion = models.CharField(max_length=100)
    fecha = models.DateField(max_length=100)
    hora = models.TimeField(max_length=100)
    id_factura = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id_usuario) + ' ' + str(self.id_comida) + ' ' + str(self.cantidad) + ' ' + str(self.total) + ' ' + str(self.direccion) + ' ' + str(self.fecha) + ' ' + str(self.hora) + ' ' + str(self.estado) + ' '
class Meta:
    db_table = 'comida'
    db_table = 'usuarios'
    db_table = 'pedidos'