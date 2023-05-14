from django.urls import path
from.import views
#solicitudes de usuario y gestionar las rutas de la aplicacion

###para redireccionar
urlpatterns = [
    path('', views.ComidaListado, name='comida'),
    
    
    
]
