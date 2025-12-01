from django.db import models
from decimal import Decimal, InvalidOperation

class Casa(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='casas/', null=True, blank=True)

    # Precio muy permisivo y seguro
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        default=Decimal("0.00")
    )

    locacion = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    apartada = models.BooleanField(default=False)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Hace el campo precio completamente seguro.
        Si llega vacío, lo convierte en 0.
        Si llega algo inválido, no truena.
        """
        try:
            if self.precio in ["", None]:
                self.precio = Decimal("0.00")
        except InvalidOperation:
            self.precio = Decimal("0.00")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Solicitud(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='pendiente')

    def __str__(self):
        return f"{self.nombre} - {self.estado}"

