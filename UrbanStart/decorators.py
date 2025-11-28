from django.shortcuts import redirect
from functools import wraps

def requiere_rol(rol_requerido):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.session.get('rol') != rol_requerido:
                return redirect('home')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def requiere_cliente(view_func):
    return requiere_rol('cliente')(view_func)

def requiere_admin(view_func):
    return requiere_rol('admin')(view_func)
