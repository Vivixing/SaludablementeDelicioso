from aiohttp import request
from django.shortcuts import render

# Create your views here.
from .models import Comida_menu

#Instanciamos las vistas genéricas de Django 
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse

#Habilitamos el uso de mensajes en Django 
from django.contrib import messages

#Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin

#Habilitamos los formularios en Django 
from django import forms


class ComidaListado(ListView):
    model = Comida_menu # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
   
    

#Crear
class ComidaCrear(SuccessMessageMixin, CreateView): 
    model = Comida_menu # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Comida_menu # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Comida Creada Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa

    # Redireccionamos a la página principal luego de crear un registro o arepa
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

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
    
    
    
