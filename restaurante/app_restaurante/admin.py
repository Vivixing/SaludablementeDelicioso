from django.contrib import admin
from .models import Comida_menu, Pedidos, Usuarios

class AdminComida(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'descripcion', 'stock', 'categoria', 'img', 'created_at', 'updated_at')
    search_fields = ('nombre', 'categoria', 'descripcion')
    list_filter = ('categoria',)

class AdminPedidos(admin.ModelAdmin):
    list_display = ('id', 'id_usuario', 'id_comida', 'cantidad', 'fecha', 'total')
    search_fields = ('id_usuario', 'id_comida', 'fecha')
    list_filter = ('fecha',)

class AdminUsuarios(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'contraseña', 'email', 'usuario', 'telefono', 'direccion', 'nacimiento', 'created_at', 'updated_at')
    search_fields = ('nombre', 'apellido', 'email', 'usuario')
    list_filter = ('nombre', 'apellido', 'email', 'usuario')

# Register your models here.
admin.site.register(Comida_menu)
admin.site.register(Usuarios)
admin.site.register(Pedidos)