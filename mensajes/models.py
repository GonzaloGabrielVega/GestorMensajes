from django.db import models

# Create your models here.
class Mensaje(models.Model):
    texto = models.TextField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self): # Devuelve una cadena del mensaje con la estructura mostrada
        return f"De: {self.remitente}, Para: {self.destinatario}"