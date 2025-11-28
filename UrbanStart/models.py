from django.db import models

# Create your models here.

class Casa(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='casas/', null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    locacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    apartada = models.BooleanField(default=False)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.titulo

from django.db import models

class Solicitud(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='pendiente')

    def __str__(self):
        return f"{self.nombre} - {self.estado}"
