# messenger/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('enviar_mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
    path('ver_mensaje/<message_id>', views.ver_mensaje, name='ver_mensaje'),
    path('borrar_mensaje/<message_id>', views.borrar_mensaje, name='borrar_mensaje'),
    path('inbox/', views.inbox, name='inbox'),
    
    # Agrega más URL para otras vistas como la bandeja de entrada, vista de mensajes, etc.
]
