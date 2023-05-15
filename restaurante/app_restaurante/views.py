from aiohttp import request
from django.shortcuts import render

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
    form = Usuarios # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos
    success_message = 'Usuario Creado Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa
    
    # Redireccionamos a la página principal luego de crear un registro o arepa
    def get_success_url(self):
     
        return reverse('leer_usuario') # Redireccionamos a la vista principal 'leer'

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
    
        try:
            user = Usuarios.objects.get(email=email)
            if user.contraseña == contraseña:
                # Autenticar manualmente al usuario
                #Primero registramos el usuario para que se guarde en la base de datos de Django
        
                # Autenticar manualmente al usuario
                if user is not None:
                    login(request, user)
                    user = authenticate(request, email=email, contraseña=contraseña)
                    # Redirigir a la página principal
                    messages.success(request, 'Bienvenido, {}!'.format(user.nombre))
                    return redirect('vista_principal')
                else:
                    messages.error(request, 'El usuario o la contraseña son incorrectos.')
            else:
                messages.error(request, 'El usuario o la contraseña son incorrectos.')
        except Usuarios.DoesNotExist:
            messages.error(request, 'El usuario o la contraseña son incorrectos.')
    return render(request, 'usuario/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def agregar_producto(request, pk):
    producto = Comida_menu.objects.filter(pk=pk).first()
    carrito = request.session.get('carrito', [])
    carrito.append((producto.id))
    request.session['carrito'] = carrito
    return redirect('mostrar_carrito')

def mostrar_carrito(request):
    carrito_ids = request.session.get('carrito', [])
    carrito = Comida_menu.objects.filter(id__in=carrito_ids)
    total = sum((producto.precio for producto in carrito))
    
    return render(request, 'vista_usuario/carritoCompra.html', {'carrito': carrito, 'total': total})

def actualizar_cantidad(request,pk):
    cantidad = request.POST.get('cantidad')
    producto = Comida_menu.objects.filter(pk=pk).first()
    carrito = request.session.get('carrito', [])
    carrito.append((producto.id))
    request.session['carrito'] = carrito
    return redirect('mostrar_carrito')

def eliminar_producto(request, pk):
    carrito = request.session.get('carrito', [])
    carrito.remove((pk))
    request.session['carrito'] = carrito
    return redirect('mostrar_carrito')

def limpiar_carrito(request):
    request.session['carrito'] = []
    return redirect('mostrar_carrito')

def login_view(request, *args, **kwargs):
    user = Usuarios.objects.all()
    ingresar = request.POST
    context={'user':user, 'nombre':'noRegistrado'}
    if(request.method == 'POST'):
        aux = Usuarios(
            nombre=ingresar.get('username'),
            email=ingresar.get('holi@gmail.com'),
            contraseña=ingresar.get('password'),
        )
        nombre=ingresar.get('username')
        if (aux.autenticarUsuario()):
            context={'user':user, 'nombre':nombre}
            messages.success(request, f'¡Bienvenido {nombre}!')
            return render(request, 'vista_principal', context,{})
        else:
            messages.info(request, 'Cuenta de usuario o contraseña invalida')
    return render(request, 'usuario/login.html', context,{'form':ingresar})