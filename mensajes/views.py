from django.shortcuts import render
from .models import Mensaje

def mensajes_recibidos(request):
    destinatario = request.GET.get('destinatario')
    if destinatario:
        mensajes = Mensaje.objects.filter(destinatario=destinatario)
    else:
        mensajes = Mensaje.objects.all()  # Mostrar todos los mensajes si no hay destinatario
    return render(request, 'mensajes/recibidos.html', {'mensajes': mensajes})
