from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nombre)
    
class Comida_menu(models.Model):  #nombre de la tabla en la Base de Datos
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=20,)
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
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    nacimiento = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.nombre) + ' ' + str(self.apellido) + ' ' 

class Pedidos(models.Model):
    id = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, to_field='id', db_column='id_usuario', on_delete=models.CASCADE)
    id_comida = models.ForeignKey(Comida_menu, to_field='id', db_column='id_comida', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField(max_length=100, auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.total = self.id_comida.precio * self.cantidad
        super(Pedidos, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id_usuario) + ' ' + str(self.id_comida) + ' ' + str(self.cantidad) + ' ' + str(self.fecha) + ' ' + str(self.total) + ' '

class DescuentoProducto(models.Model):
    id = models.IntegerField(primary_key=True)
    id_comida = models.ForeignKey(Comida_menu, to_field='id', db_column='id_comida', on_delete=models.CASCADE)
    descuento = models.FloatField()
    fecha_inicio = models.DateField(max_length=100)
    fecha_fin = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_comida) + ' ' + str(self.descuento) + ' ' + str(self.fecha_inicio) + ' ' + str(self.fecha_fin) + ' '

class DescuentoCumple(models.Model):
    id = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, to_field='id', db_column='id_usuario', on_delete=models.CASCADE)
    descuento = models.FloatField()
    fecha_inicio = models.DateField(max_length=100)
    fecha_fin = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_usuario) + ' ' + str(self.descuento) + ' ' + str(self.fecha_inicio) + ' ' + str(self.fecha_fin) + ' '

class DescuentoCategoria(models.Model):
    id = models.IntegerField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, to_field='id', db_column='id_categoria', on_delete=models.CASCADE)
    descuento = models.FloatField()
    fecha_inicio = models.DateField(max_length=100)
    fecha_fin = models.DateField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_usuario) + ' ' + str(self.descuento) + ' ' + str(self.fecha_inicio) + ' ' + str(self.fecha_fin) + ' '
class Meta:
    db_table = 'comida'
    db_table = 'usuarios'
    db_table = 'pedidos'