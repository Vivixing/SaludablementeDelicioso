from django.contrib import admin
from .models import Comida_menu, Pedidos, Usuarios, Categoria

class AdminComida(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'descripcion', 'stock', 'categoria', 'img', 'created_at', 'updated_at')
    search_fields = ('nombre', 'categoria', 'descripcion')
    list_filter = ('categoria','nombre')


class AdminPedidos(admin.ModelAdmin):
    list_display = ('id', 'id_usuario', 'id_comida', 'cantidad', 'fecha', 'total')
    search_fields = ('id_usuario', 'id_comida', 'fecha')
    list_filter = ('fecha','id_usuario')
'''
class AdminUsuarios(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'contraseña', 'email', 'telefono', 'direccion', 'nacimiento', 'created_at', 'updated_at')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('nombre', 'apellido', 'email')
'''
# Register your models here.
admin.site.register(Comida_menu, AdminComida)
admin.site.register(Pedidos, AdminPedidos)
admin.site.register(Usuarios)
admin.site.register(Categoria)
