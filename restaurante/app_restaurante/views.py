import datetime
import random
from aiohttp import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from datetime import date
from .forms import LoginForm, UsuarioForm
from itertools import zip_longest

# Create your views here.
from .models import Comida_menu, Usuarios, Pedidos, Categoria, DescuentoCategoria, DescuentoProducto, DescuentoCumple
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
    model = Usuarios # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'

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
    model = Pedidos # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'

#Crear
class PedidoCrear(SuccessMessageMixin, CreateView):
    model = Pedidos # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Pedidos # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos
    success_message = 'Pedido Creado Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa

    #
    # Redireccionamos a la página principal luego de crear un registro o arepa
    def get_success_url(self):
        return reverse('leer_pedido') # Redireccionamos a la vista principal 'leer'

#Leer, mostrar los detalles de la comida
class PedidoDetalle(DetailView):
    model = Pedidos # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'

#Actualizar por formulario
class PedidoActualizar(SuccessMessageMixin, UpdateView):
    model = Pedidos # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Pedidos # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos
    success_message = 'Pedido Actualizado Correctamente!' # Mostramos este Mensaje luego de Editar un Arepa

    # Redireccionamos a la página principal luego de actualizar un registro o arepa
    def get_success_url(self):
        return reverse('leer_pedido') # Redireccionamos a la vista principal 'leer'

#Eliminar
class PedidoEliminar(SuccessMessageMixin, DeleteView):
    model = Pedidos
    form = Pedidos
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o arepa
    def get_success_url(self):
        success_message = 'Pedido Eliminado Correctamente!' # Mostramos este Mensaje luego de Eliminar una Arepa
        messages.success (self.request, (success_message))
        return reverse('leer_pedido') # Redireccionamos a la vista principal 'leer'
    
class Index(ListView):
    model = Comida_menu
    

class VistaPrincipalView(TemplateView):
    template_name = 'vista_usuario/vistaPrincipal.html'

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

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')
    
        # Retrieve the user object based on the provided email
        try:
            user = Usuarios.objects.get(email=email)
        except Usuarios.DoesNotExist:
            user = None

        if user is not None and user.check_password(contraseña):
            # Authenticate the user
            authenticated_user = authenticate(request, username=user.email, password=contraseña)

            if authenticated_user is not None:
                # Login the authenticated user
                login(request, authenticated_user)
                
                # Redirect to the main view
                return redirect('./vista_usuario/vista_principal')
            else:
                messages.error(request, 'Failed to authenticate user.')
        else:
            messages.error(request, 'Incorrect email or password.')

    return render(request, 'usuario/login.html')

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

def mostrar_carrito(request):
    carrito_ids = request.session.get('carrito', [])
    carrito = Comida_menu.objects.filter(id__in=carrito_ids)
    total = sum((producto.precio * carrito_ids.count(producto.id) for producto in carrito))
    #Creamos una lista con las cantidades de cada producto
    return render(request, 'vista_usuario/carritoCompra.html', {'carrito': carrito, 'total': total})

def actualizar_cantidad(request, pk):
    carrito = request.session.get('carrito', [])
    cantidad_actualizada = request.POST.get('cantidad')
    cantidad_actualizada = int(cantidad_actualizada)
    Usuario= Usuarios.objects.get(usuario=request.user)
    if cantidad_actualizada>=1:
        carrito.append(pk)# Agregar solo el ID del producto al carrito
    if cantidad_actualizada < 1:
        carrito.remove(pk)
        
    # Obtener el pedido asociado al producto y al usuario actual
    pedido = Pedidos.objects.get(id_comida=pk, id_usuario=Usuario, fecha=datetime.date.today())
    pedido.cantidad = cantidad_actualizada
    pedido.save()

    request.session['carrito'] = carrito
    return redirect('mostrar_carrito')

def eliminar_producto(request, pk):
    carrito = request.session.get('carrito', [])
    #Recorremos el carrito y eliminamos todos los productos con el id que le pasamos
    for i in carrito:
        if i == pk:
            carrito.remove(i)
            
    request.session['carrito'] = carrito
    
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

def factura(request):
    usuario = Usuarios.objects.get(usuario=request.user)
    pedidos = Pedidos.objects.filter(id_usuario=usuario, fecha=datetime.date.today())
    comidas_ids = pedidos.values_list('id_comida', flat=True)
    comida_menu = Comida_menu.objects.filter(id__in=comidas_ids)

    precios_calculados = []
    for pedido in pedidos:
        precio_total = pedido.id_comida.precio * pedido.cantidad
        precios_calculados.append(precio_total)

    fecha = datetime.date.today()
    total = sum(precios_calculados, 0)

    # Zip the pedidos and precios_calculados lists
    zipped_data = zip_longest(pedidos, precios_calculados)

    return render(request, 'vista_usuario/factura.html', {'zipped_data': zipped_data, 'comida_menu': comida_menu, 'fecha': fecha, 'usuario': usuario, 'total': total, })
