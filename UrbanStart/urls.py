from django.urls import path
from . import views

from .views import (
    admin_casas,
    admin_casa_crear,
    admin_casa_editar,
    admin_casa_eliminar,
)

urlpatterns = [
    # RUTAS PÚBLICAS / CLIENTE
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('buscar_casas/', views.buscar_casas, name='buscar_casas'),
    path('rol/<str:rol>/', views.seleccionar_rol, name='seleccionar_rol'),

    # CRUD ADMIN CASAS
    path("panel-admin/catalogo/", admin_casas, name="admin_casas"),
    path("panel-admin/catalogo/nueva/", admin_casa_crear, name="admin_casa_crear"),
    path("panel-admin/catalogo/<int:id>/editar/", admin_casa_editar, name="admin_casa_editar"),
    path("panel-admin/catalogo/<int:id>/eliminar/", admin_casa_eliminar, name="admin_casa_eliminar"),

    # ADMIN SOLICITUDES
    path('panel-admin/solicitudes/', views.admin_solicitudes, name='admin_solicitudes'),
]




