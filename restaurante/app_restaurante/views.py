import datetime
import random
from aiohttp import request
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from datetime import date, timedelta

from django.views import View
from .forms import LoginForm, UsuarioForm
from itertools import zip_longest

# Create your views here.
from .models import Comida_menu, InformacionVenta, Delivery, Usuarios, Pedidos, Categoria, DescuentoCategoria, DescuentoProducto, DescuentoCumple
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
#Instanciamos las vistas genéricas de Django 
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView


#Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse

#Habilitamos el uso de mensajes en Django 
from django.contrib import messages

#Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin

#Habilitamos los formularios en Django 
from django import forms
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

class CategoriaListado(ListView):
    model = Categoria # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return render(request, self.template_name)
        else:
            return redirect('vista_principal')
        
class CategoriaCrear(SuccessMessageMixin, CreateView):
    model = Categoria # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Categoria # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Categoria Creada Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa
        
    # Redireccionamos a la página principal luego de crear un registro o arepa
    def get_success_url(self):        
        return reverse('leer_categoria')

class CategoriaActualizar(SuccessMessageMixin, UpdateView):
    model = Categoria # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Categoria # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Categoria Actualizada Correctamente!' # Mostramos este Mensaje luego de Editar un Arepa 

        
    # Redireccionamos a la página principal luego de actualizar un registro o arepa
    def get_success_url(self):               
        return reverse('leer_categoria') # Redireccionamos a la vista principal 'leer'

class CategoriaDetalle(DetailView):
    model = Categoria # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'

        
class CategoriaEliminar(SuccessMessageMixin, DeleteView):
    model = Categoria
    form = Categoria
    fields = "__all__"     
        
    # Redireccionamos a la página principal luego de eliminar un registro o arepa
    def get_success_url(self): 
        success_message = 'Categoria Eliminada Correctamente!' # Mostramos este Mensaje luego de Eliminar una Arepa 
        messages.success (self.request, (success_message))       
        return reverse('leer_categoria') # Redireccionamos a la vista principal 'leer'

class ComidaListado(ListView):
    model = Comida_menu # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    

    
#Crear
class ComidaCrear(SuccessMessageMixin, CreateView): 
    model = Comida_menu # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Comida_menu# Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Comida Creada Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa

        
    # Redireccionamos a la página principal luego de crear un registro o arepa
    def get_success_url(self):        
        return reverse('leer') 

#Leer, mostrar los detalles de la comida
class ComidaDetalle(DetailView): 
    model = Comida_menu # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 

#Actualizar por formulario
class ComidaActualizar(SuccessMessageMixin, UpdateView): 
    model = Comida_menu # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    form = Comida_menu # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Comida Actualizada Correctamente!' # Mostramos este Mensaje luego de Editar un Arepa 
    

    # Redireccionamos a la página principal luego de actualizar un registro o arepa
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
#Eliminar 
class ComidaEliminar(SuccessMessageMixin, DeleteView): 
    model = Comida_menu 
    form = Comida_menu
    fields = "__all__"     

        
    # Redireccionamos a la página principal luego de eliminar un registro o arepa
    def get_success_url(self): 
        success_message = 'Comida Eliminada Correctamente!' # Mostramos este Mensaje luego de Eliminar una Arepa 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class UsuarioListado(ListView):
    model = Usuarios # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'  # Ordenar por el campo fecha_nacimiento
    
        
class UsuarioListadoCumple(ListView):
    model = Usuarios # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    ordering = 'nacimiento'  # Ordenar por el campo fecha_nacimiento

        
    def get_queryset(self):
        queryset = super().get_queryset()
        today = date.today()
        queryset = queryset.order_by(
            'nacimiento__month',
            'nacimiento__day'
        )
        return queryset

#Crear
class UsuarioCrear(SuccessMessageMixin, CreateView):
    model = Usuarios # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form_class = UsuarioForm # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    def form_valid(self, form):
            form.save()
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            usuario = authenticate(username=usuario, password=password)
            telefono = form.cleaned_data.get('telefono')
            direccion = form.cleaned_data.get('direccion')
            nacimiento = form.cleaned_data.get('nacimiento')
            usuarioBD = Usuarios(telefono=telefono, direccion=direccion, nacimiento=nacimiento, usuario=usuario)
            usuarioBD.save()

            #Inmediatamente despues de crear el usuario, se creará su descuento de cumpleaños
            fecha_inicio = date(date.today().year, nacimiento.month, nacimiento.day)
            fecha_fin = fecha_inicio + timedelta(days=1)

            descuentoCumple = DescuentoCumple(id_usuario=usuarioBD, descuento=0.15, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
            descuentoCumple.save()

            login(self.request, usuario)
            return redirect('vista_principal')
    #Leer, mostrar los detalles de la comida
class UsuarioDetalle(DetailView):
    model = Usuarios # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'

#Actualizar por formulario
class UsuarioActualizar(SuccessMessageMixin, UpdateView):
    model = Usuarios # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Usuarios # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos
    success_message = 'Usuario Actualizado Correctamente!' # Mostramos este Mensaje luego de Editar un Arepa

    # Redireccionamos a la página principal luego de actualizar un registro o arepa
    def get_success_url(self):
        return reverse('leer_usuario') # Redireccionamos a la vista principal 'leer'

#Eliminar
class UsuarioEliminar(SuccessMessageMixin, DeleteView):
    model = Usuarios
    form = Usuarios
    fields = "__all__"

        
    # Redireccionamos a la página principal luego de eliminar un registro o arepa
    def get_success_url(self):
        success_message = 'Usuario Eliminado Correctamente!' # Mostramos este Mensaje luego de Eliminar una Arepa
        messages.success (self.request, (success_message))
        return reverse('leer_usuario') # Redireccionamos a la vista principal 'leer'

class PedidoListado(ListView):
    model = Delivery # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'

#Crear
class PedidoCrear(SuccessMessageMixin, CreateView):
    model = Delivery # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Delivery # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos
    success_message = 'Pedido Creado Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa
    
    #
    # Redireccionamos a la página principal luego de crear un registro o arepa
    def get_success_url(self):
        return reverse('leer_pedido') # Redireccionamos a la vista principal 'leer'

#Leer, mostrar los detalles de la comida
class PedidoDetalle(DetailView):
    model = Delivery # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'

#Actualizar por formulario
class PedidoActualizar(SuccessMessageMixin, UpdateView):
    model = Delivery # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Delivery # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos
    success_message = 'Pedido Actualizado Correctamente!' # Mostramos este Mensaje luego de Editar un Arepa

        
    # Redireccionamos a la página principal luego de actualizar un registro o arepa
    def get_success_url(self):
        return reverse('leer_pedido') # Redireccionamos a la vista principal 'leer'

#Eliminar
class PedidoEliminar(SuccessMessageMixin, DeleteView):
    model = Delivery
    form = Delivery
    fields = "__all__"
        
    # Redireccionamos a la página principal luego de eliminar un registro o arepa
    def get_success_url(self):
        success_message = 'Pedido Eliminado Correctamente!' # Mostramos este Mensaje luego de Eliminar una Arepa
        messages.success (self.request, (success_message))
        return reverse('leer_pedido') # Redireccionamos a la vista principal 'leer'


class Index(View):
    template_name = 'admin/indexAdmi.html'
    #Verificamos si el usuario es administrador
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return render(request, self.template_name)
        else:
            return redirect('vista_principal')

class InformacionVentaListado(ListView):
    model = InformacionVenta
    context_object_name = 'informacionVentas'

    def get_queryset(self):
        return InformacionVenta.objects.all().order_by('-cantidad')


class VistaPrincipalView(TemplateView):
    template_name = 'vista_usuario/vistaPrincipal.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            # Realizar búsqueda y pasar los resultados a la plantilla
            productos = Comida_menu.objects.filter(nombre__icontains=query)
            context['resultados'] = productos
        return context


def vista_vegetariano(request):
    items = Comida_menu.objects.filter(categoria='1')
    context = {'items': items}
    print(items)
    return render(request, 'vista_usuario/vistaVegetariana.html', context)

def vista_diabeticos(request):
    items = Comida_menu.objects.filter(categoria='2')
    context = {'items': items}
    print(items)
    return render(request, 'vista_usuario/vistaDiab.html', context)

def vista_veganos(request):
    items = Comida_menu.objects.filter(categoria='3')
    context = {'items': items}
    print(items)
    return render(request, 'vista_usuario/vistaVegano.html', context)

def vista_bebidas(request):
    items = Comida_menu.objects.filter(categoria='4')
    context = {'items': items}
    print(items)
    return render(request, 'vista_usuario/vistaBebidas.html', context)

def vista_postres(request):
    items = Comida_menu.objects.filter(categoria='5')
    context = {'items': items}
    print(items)
    return render(request, 'vista_usuario/vistaPostre.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def agregar_producto(request, pk):
    producto = Comida_menu.objects.filter(pk=pk).first()
    carrito = request.session.get('carrito', [])
    carrito.append(pk)  # Agregar solo el ID del producto al carrito
    request.session['carrito'] = carrito
    cantidad = request.POST.get('cantidad')
    if cantidad is None:
        cantidad = 1
    
    # Obtener instancia de Usuarios del usuario actual
    usuario = Usuarios.objects.get(usuario=request.user)

    # Crear instancia de Pedidos
    pedido = Pedidos(
        id_usuario=usuario,
        id_comida=producto,
        cantidad=cantidad,
    )
    pedido.save()
    
    return redirect('mostrar_carrito')

@login_required
def mostrar_carrito(request):
    carrito_ids = request.session.get('carrito', [])
    carrito = Comida_menu.objects.filter(id__in=carrito_ids)
    total = sum((producto.precio * carrito_ids.count(producto.id) for producto in carrito))
    #Creamos una lista para guardar la cantidad de que cada producto se encuentra en el carrito
    cantidad = []
    for producto in carrito:
        cantidad.append(carrito_ids.count(producto.id))
    #Relacionamos cada producto con su cantidad
    zipped_data = zip_longest(carrito, cantidad)
    return render(request, 'vista_usuario/carritoCompra.html', {'carrito': carrito, 'total': total, 'zipped_data': zipped_data})

def actualizar_cantidad(request, pk):

    carrito = request.session.get('carrito', [])
    cantidad_actualizada = request.POST.get('cantidad')
    cantidad_actualizada = int(cantidad_actualizada)
    Usuario= Usuarios.objects.get(usuario=request.user)
    #Verificamos que la cantidad que ingresa el usuario no supere el stock del producto
    producto = Comida_menu.objects.get(pk=pk)

    if int(cantidad_actualizada) > int(producto.stock):
        messages.error(request, 'La cantidad ingresada supera el stock del producto')

    
    else:
        # Obtener el pedido asociado al producto y al usuario actual
        pedido = Pedidos.objects.get(id_comida=pk, id_usuario=Usuario, fecha=datetime.date.today())
        pedido.cantidad = cantidad_actualizada
        pedido.save()
        diferencia = carrito.count(pk) - pedido.cantidad
        if diferencia < 0:
            for i in range(abs(diferencia)):
                carrito.append(pk)
        elif diferencia > 0:
            for i in range(abs(diferencia)):
                carrito.remove(pk)
        producto.save()
        request.session['carrito'] = carrito
    return redirect('mostrar_carrito')

def eliminar_producto(request, pk):
    carrito = request.session.get('carrito', [])
    # Creamos una lista auxiliar para almacenar los productos que no se eliminarán
    carrito_actualizado = []
    
    # Recorremos el carrito y agregamos los productos que no coinciden con el ID a eliminar
    for producto_id in carrito:
        if producto_id != pk:
            carrito_actualizado.append(producto_id)
    
    # Actualizamos el carrito en la sesión con la lista actualizada
    request.session['carrito'] = carrito_actualizado
    
    # Obtener el usuario actual
    usuario = Usuarios.objects.get(usuario=request.user)
    
    # Eliminar los elementos de pedido asociados al producto eliminado y al usuario actual
    Pedidos.objects.filter(id_comida=pk, id_usuario=usuario).delete()
    
    return redirect('mostrar_carrito')


def limpiar_carrito(request):
    carrito = request.session.get('carrito', [])
    request.session['carrito'] = []
    
    # Obtener el usuario actual
    usuario = Usuarios.objects.get(usuario=request.user)
    
    # Eliminar todos los elementos de pedido asociados a los productos en el carrito y al usuario actual
    Pedidos.objects.filter(id_comida__in=carrito, id_usuario=usuario, fecha= datetime.date.today()).delete()
    
    return redirect('mostrar_carrito')

class Login_view(LoginView):
    template_name = 'usuario/login.html'
    
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def factura(request):
    #Limpiamos el carrito
    carrito = request.session.get('carrito', [])
    request.session['carrito'] = []

    descuento = 0
    descuentoCategoria = 0
    descuentoProducto = 0
    descuentoCumple = 0

    usuario = Usuarios.objects.get(usuario=request.user)
    pedidos = Pedidos.objects.filter(id_usuario=usuario, fecha=datetime.date.today())
    comidas_ids = pedidos.values_list('id_comida', flat=True)
    comida_menu = Comida_menu.objects.filter(id__in=comidas_ids)

    precios_calculados = []
    for pedido in pedidos:
        precio_total = pedido.id_comida.precio * pedido.cantidad
        pedido.id_comida.stock = int(pedido.id_comida.stock) - pedido.cantidad
        pedido.id_comida.save()
        precios_calculados.append(precio_total)

    #Obtenemos la fecha actual
    fecha = datetime.date.today()
    #Verificamos si el usuario cumple años ese día para aplicarle el descuento
    cumple = DescuentoCumple.objects.filter(id_usuario=usuario, fecha_inicio=fecha).exists()
    if cumple:
        descuentoCumple= DescuentoCumple.objects.get(id_usuario=usuario, fecha_inicio=fecha)
        descuentoCumple = descuentoCumple.descuento
    else:
        descuentoCumple = 0
    #Verificamos si hay descuento por categoría o por producto
    for pedido in pedidos:
        descuentoCategoria = DescuentoCategoria.objects.filter(id_categoria=pedido.id_comida.categoria).exists()
        if descuentoCategoria:
            descuentoCategoria = DescuentoCategoria.objects.get(id_categoria=pedido.id_comida.categoria)
            descuentoCategoria = descuentoCategoria.descuento
        else:
            descuentoCategoria = 0

        descuentoProducto = DescuentoProducto.objects.filter(id_comida=pedido.id_comida).exists()
        if descuentoProducto:
            descuentoProducto = DescuentoProducto.objects.get(id_comida=pedido.id_comida)
            descuentoProducto = descuentoProducto.descuento
        else:
            descuentoProducto = 0
    #Se aplica el descuento que sea mayor
    if descuentoCumple > descuentoCategoria and descuentoCumple > descuentoProducto:
        descuento = descuentoCumple
    
    elif descuentoCategoria > descuentoCumple and descuentoCategoria > descuentoProducto:
        descuento = descuentoCategoria
    
    elif descuentoProducto > descuentoCumple and descuentoProducto > descuentoCategoria:
        descuento = descuentoProducto

    subtotal = sum(precios_calculados, 0)
    resta = sum(precios_calculados, 0)*descuento
    total = sum(precios_calculados, 0) - resta
    resta= int(resta)
    total = int(total)
    fac_id = random.randint(1, 1000000)
    # Zip the pedidos and precios_calculados lists
    zipped_data = zip_longest(pedidos, precios_calculados)

    # Eliminar los elementos de pedido asociados a los productos en el carrito y al usuario actual
    Pedidos.objects.filter(id_usuario=usuario, fecha= datetime.date.today()).delete()
    

    #Agregamos la información de la venta a la base de datos de ventas
    for pedido in pedidos:
        #Verificamos si el producto ya se encuentra en la base de datos de ventas
        delivery = Delivery(id_usuario=usuario,id_comida=pedido.id_comida, cantidad=pedido.cantidad, fecha=fecha, totalFactura=total, direccion=usuario.direccion, id_factura=fac_id, hora=datetime.datetime.now())
        delivery.save()

        if InformacionVenta.objects.filter(id_comida=pedido.id_comida).exists():
            #Si el producto ya se encuentra en la base de datos, se actualiza la cantidad y el total
            informacionVenta = InformacionVenta.objects.get(id_comida=pedido.id_comida)
            informacionVenta.cantidad = informacionVenta.cantidad + pedido.cantidad
            informacionVenta.totalVenta = informacionVenta.totalVenta + pedido.id_comida.precio * pedido.cantidad
            informacionVenta.save()
        else:
            informacionVenta = InformacionVenta(id_comida=pedido.id_comida, cantidad=pedido.cantidad, fecha=fecha, totalVenta= pedido.id_comida.precio * pedido.cantidad)
            informacionVenta.save()
    return render(request, 'vista_usuario/factura.html', { 'zipped_data': zipped_data, 'comida_menu': comida_menu, 'fecha': fecha, 'usuario': usuario, 'total': total, 'descuento': resta, 'subtotal': subtotal, 'fac_id': fac_id})

