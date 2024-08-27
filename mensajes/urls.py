from django.urls import path
from .views import mensajes_recibidos

urlpatterns = [
    path('recibidos/', mensajes_recibidos, name='recibidos'),
]
