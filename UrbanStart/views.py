from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
import os
from dotenv import load_dotenv
from .models import Casa, Solicitud
from .decorators import requiere_cliente

load_dotenv()

# ----------------------------------------
# Páginas públicas
# ----------------------------------------

def home(request):
    return render(request, "UrbanStart/home.html")


def contact(request):
    success = False
    error = False
    name = ''
    email = ''
    message = ''

    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        try:
            Solicitud.objects.create(
                nombre=name,
                email=email,
                mensaje=message,
                estado='pendiente'
            )
            success = True
            name = ''
            email = ''
            message = ''
        except Exception as e:
            error = True
            print(f"Error al enviar correo: {e}")

    context = {
        'success': success,
        'error': error,
        'name': name,
        'email': email,
        'message': message
    }

    return render(request, "UrbanStart/contact.html", context)


def about(request):
    return render(request, "UrbanStart/about.html")


# ----------------------------------------
# Sistema de roles
# ----------------------------------------

@requiere_cliente
def catalogo(request):
    casas = Casa.objects.all()
    return render(request, "UrbanStart/catalogo.html", {"casas": casas})


def seleccionar_rol(request, rol):
    if rol in ['cliente', 'admin']:
        request.session['rol'] = rol
        request.session.save()

        return redirect('catalogo' if rol == 'cliente' else 'admin_casas')

    return redirect('home')


# ----------------------------------------
# CRUD ADMIN
# ----------------------------------------

# Dashboard + listado
def admin_casas(request):
    casas = Casa.objects.all()
    
    context = {
        "casas": casas,
        "total_casas": casas.count(),
        "total_solicitudes": Solicitud.objects.count(),
        "solicitudes_pendientes": Solicitud.objects.filter(estado='pendiente').count(),
    }
    return render(request, "UrbanStart/admin_casas.html", context)


# Crear casa con imagen
def admin_casa_crear(request):
    if request.method == "POST":
        Casa.objects.create(
            titulo=request.POST["titulo"],
            descripcion=request.POST["descripcion"],
            precio=request.POST["precio"],
            imagen=request.FILES.get("imagen")  # 🔶 agregar imagen
        )
        return redirect("admin_casas")

    return render(request, "UrbanStart/admin_casa_form.html")



# Editar casa con imagen
def admin_casa_editar(request, id):
    casa = get_object_or_404(Casa, id=id)

    if request.method == "POST":
        casa.titulo = request.POST["titulo"]
        casa.descripcion = request.POST["descripcion"]
        casa.precio = request.POST["precio"]

        #  Si el usuario sube una nueva imagen, se reemplaza
        if request.FILES.get("imagen"):
            casa.imagen = request.FILES["imagen"]

        casa.save()
        return redirect("admin_casas")

    return render(request, "UrbanStart/admin_casa_form.html", {"casa": casa})


# Eliminar casa
def admin_casa_eliminar(request, id):
    casa = get_object_or_404(Casa, id=id)
    casa.delete()
    return redirect("admin_casas")


# Solicitudes admin
def admin_solicitudes(request):
    solicitudes = Solicitud.objects.all().order_by('-timestamp')
    return render(request, 'UrbanStart/admin_solicitudes.html', {'solicitudes': solicitudes})


