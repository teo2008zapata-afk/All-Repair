from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('servicios/', views.servicios, name='servicios'),
    path('blog/', views.blog, name='blog'),
    path('contactanos/', views.contactanos, name='contactanos'),

    path('administrador/', views.dashboard, name='dashboard'),
    path('administrador/login/', views.iniciar_sesion, name='login'),
    path('administrador/logout/', views.cerrar_sesion, name='logout'),

    path('repuestos/crear/', views.crear, name='repuesto_crear'),
    path('repuestos/lista/', views.listar, name='repuesto_lista'),
    path('repuestos/detalle/<id>/', views.detalle, name='repuesto_detalle'),
    path('repuestos/editar/<id>/', views.editar, name='repuesto_editar'),
    path('repuestos/eliminar/<id>/', views.eliminar, name='repuesto_eliminar'),

    path('servicios/crear/', views.crear_servicio, name='servicio_crear'),
    path('servicios/lista/', views.listar_servicios, name='servicio_lista'),
    path('servicios/detalle/<id>/', views.detalle_servicio, name='servicio_detalle'),
    path('servicios/editar/<id>/', views.editar_servicio, name='servicio_editar'),
    path('servicios/eliminar/<id>/', views.eliminar_servicio, name='servicio_eliminar'),
]
