from django.shortcuts import render
from django.core.mail import EmailMessage
from HomeKey_Central.settings import EMAIL_HOST_USER


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

        email_subject = f"Nuevo mensaje de contacto de {name}"
        email_body = f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}"

        try:
            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=EMAIL_HOST_USER,
                to=[EMAIL_HOST_USER],
                reply_to=[email]
            )
            email_message.send(fail_silently=False)
            success = True
            # Limpiar campos después de enviar
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
