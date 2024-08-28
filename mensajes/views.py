from django.shortcuts import render
from .models import Mensaje

def mensajes_recibidos(request):
    destinatario = request.GET.get('destinatario') #obtiene el destinatario del formulario
    if destinatario:
        mensajes = Mensaje.objects.filter(destinatario=destinatario).order_by('-fecha_envio') # '-fecha_envio' ordena los mensajes mas recientes
    else:
        mensajes = Mensaje.objects.all().order_by('-fecha_envio')  # Mostrar todos los mensajes si no hay destinatario
    return render(request, 'mensajes/recibidos.html', {'mensajes': mensajes})
