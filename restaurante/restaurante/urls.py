"""restaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
#from django.urls import include
from  app_restaurante.views import CategoriaListado, UsuarioListadoCumple, CategoriaDetalle, CategoriaActualizar, CategoriaCrear, CategoriaEliminar, ComidaListado, InformacionVentaListado, eliminar_producto, limpiar_carrito, actualizar_cantidad,agregar_producto, mostrar_carrito,  vista_vegetariano, logout_view, LoginView, Index, ComidaDetalle,ComidaCrear,ComidaActualizar,ComidaEliminar, UsuarioActualizar, UsuarioCrear, UsuarioDetalle, UsuarioEliminar, UsuarioListado, PedidoActualizar, PedidoCrear, PedidoDetalle, PedidoEliminar, PedidoListado, VistaPrincipalView, vista_bebidas, vista_diabeticos, vista_postres, vista_veganos, factura, DescuentoCategoria,DescuentoCategoriaActualizar,DescuentoCategoriaCrear, DescuentoCategoriaDetalle, DescuentoCategoriaEliminar,DescuentoCategoriaListado, DescuentoProducto, DescuentoProductoActualizar, DescuentoProductoCrear, DescuentoProductoDetalle, DescuentoProductoEliminar, DescuentoProductoListado
#from .views import principal
#from .views import principal
#from app_restaurante.views import principal
from django.views.generic import RedirectView
from django.views.static import serve








urlpatterns = [
    #urls para la vista del usuario
    path('', RedirectView.as_view(url='vista_usuario/vistaPrincipal', permanent=False)),
    path('vista_usuario/',  RedirectView.as_view(url='vistaPrincipal', permanent=False)),
    path('vista_usuario/vistaPrincipal', VistaPrincipalView.as_view(), name='vista_principal'),
    path('vista_usuario/vistaVegetariana', vista_vegetariano , name='vistaVegetariana'),
    path('vista_usuario/vistaVegano',vista_veganos, name='vistaVegano'),
    path('vista_usuario/vistaDiab', vista_diabeticos, name='vistaDiab'),
    path('vista_usuario/vistaBebidas',vista_bebidas, name='vistaBebidas'),
    path('vista_usuario/vistaPostre', vista_postres, name='vistaPostre'),
    path('vista_usuario/carritoCompra', VistaPrincipalView.as_view(template_name="vista_usuario/carritoCompra.html"), name='carritoCompra'),

    #Urls del login y el registro
    path('usuario/crear', UsuarioCrear.as_view(template_name = "usuario/crear.html"), name='crearUsuario'),
    path('usuario/login', LoginView.as_view(template_name="usuario/login.html"), name='login'),
    path('usuario/logout', logout_view, name='logout'),

    #Urls del carrito de compras y la factura
    path('vista_usuario/agregar_producto/<int:pk>/', agregar_producto, name='agregar_producto'),
    path('vista_usuario/mostrar_carrito/', mostrar_carrito, name='mostrar_carrito'),
    path('vista_usuario/actualizar_cantidad/<int:pk>/', actualizar_cantidad, name='actualizar_cantidad'),
    path('vista_usuario/eliminar_producto/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    path('vista_usuario/limpiar_carrito/', limpiar_carrito, name='limpiar_carrito'),
    path('vista_usuario/factura/', factura, name='factura'),
    
    
    #urls para la vista del administrador 
    path('admin/', admin.site.urls),
    path('principalAdmi/', Index.as_view(), name='principalAdmi'),
    path('administrador/informacionVenta/', InformacionVentaListado.as_view(template_name = "admin/informacionVenta.html"), name='informacionVenta'),

    path('categoria/', CategoriaListado.as_view(template_name = "categoria/categoria.html"), name='categoria'),
    path('categoria/detalle/<int:pk>', CategoriaDetalle.as_view(template_name = "categoria/detalles.html"), name='detallesCategoria'),
    path('categoria/crear', CategoriaCrear.as_view(template_name = "categoria/crear.html"), name='crearCategoria'),
    
    path('comida/', ComidaListado.as_view(template_name = "comida/comida.html"), name='leer'),
    path('comida/detalle/<int:pk>', ComidaDetalle.as_view(template_name = "comida/detalles.html"), name='detalles'),
    path('comida/crear', ComidaCrear.as_view(template_name = "comida/crear.html"), name='crear'),
    path('comida/actualizar/<int:pk>', ComidaActualizar.as_view(template_name = "comida/actualizar.html"), name='actualizar'), 
    path('comida/eliminar/<int:pk>', ComidaEliminar.as_view(template_name= "comida/eliminar.html"), name='eliminar'),

    path('usuario/', UsuarioListado.as_view(template_name = "usuario/usuario.html"), name='leer_usuario'),
    path('usuario/cumple', UsuarioListadoCumple.as_view(template_name = "usuario/usuarioCumple.html"), name='leer_usuarioCumple'),
    path('usuario/detalle/<int:pk>', UsuarioDetalle.as_view(template_name = "usuario/detalles.html"), name='detallesUsuario'),
    path('usuario/actualizar/<int:pk>', UsuarioActualizar.as_view(template_name = "usuario/actualizar.html"), name='actualizarUsuario'),
    path('usuario/eliminar/<int:pk>', UsuarioEliminar.as_view(template_name= "usuario/eliminar.html"), name='eliminarUsuario'),

    path('pedido/', PedidoListado.as_view(template_name = "pedido/pedido.html"), name='leer_pedido'),
    path('pedido/detalle/<int:pk>', PedidoDetalle.as_view(template_name = "pedido/detalles.html"), name='detallesPedido'),
    path('pedido/crear', PedidoCrear.as_view(template_name = "pedido/crear.html"), name='crearPedido'),
    path('pedido/actualizar/<int:pk>', PedidoActualizar.as_view(template_name = "pedido/actualizar.html"), name='actualizarPedido'),
    path('pedido/eliminar/<int:pk>', PedidoEliminar.as_view(template_name= "pedido/eliminar.html"), name='eliminarPedido'),
    
    path('descuentoCategoria/', DescuentoCategoriaListado.as_view(template_name = "descuentoCategoria/descuentoCategoria.html"), name='leer_descuentoCategoria'),
    path('descuentoCategoria/detalle/<int:pk>', DescuentoCategoriaDetalle.as_view(template_name = "descuentoCategoria/detallesDescuentoCat.html"), name='detallesDescuentoCategoria'),
    path('descuentoCategoria/crear', DescuentoCategoriaCrear.as_view(template_name = "descuentoCategoria/crearDescuentoCat.html"), name='crearDescuentoCategoria'),
    path('descuentoCategoria/actualizar/<int:pk>', DescuentoCategoriaActualizar.as_view(template_name = "descuentoCategoria/actualizarDescuentoCat.html"), name='actualizarDescuentoCategoria'),
    path('descuentoCategoria/eliminar/<int:pk>', DescuentoCategoriaEliminar.as_view(template_name= "descuentoCategoria/eliminarDescuentoCat.html"), name='eliminarDescuentoCategoria'),

    path('descuentoProducto/', DescuentoProductoListado.as_view(template_name = "descuentoProducto/descuentoProducto.html"), name='leer_descuentoProducto'),
    path('descuentoProducto/detalle/<int:pk>', DescuentoProductoDetalle.as_view(template_name = "descuentoProducto/detallesDescuentoProduc.html"), name='detallesDescuentoProducto'),
    path('descuentoProducto/crear', DescuentoProductoCrear.as_view(template_name = "descuentoProducto/crearDescuentoProduc.html"), name='crearDescuentoProducto'),
    path('descuentoProducto/actualizar/<int:pk>', DescuentoProductoActualizar.as_view(template_name = "descuentoProducto/actualizarDescuentoProduc.html"), name='actualizarDescuentoProducto'),
    path('descuentoProducto/eliminar/<int:pk>', DescuentoProductoEliminar.as_view(template_name= "descuentoProducto/eliminarDescuentoProduc.html"), name='eliminarDescuentoProducto'),
    

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root':settings.MEDIA_ROOT,
    })
    
]
