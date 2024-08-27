from django.urls import path
from mensajes.views import mensajes_recibidos

urlpatterns = [
    path('recibidos/', mensajes_recibidos, name='recibidos'),
]
