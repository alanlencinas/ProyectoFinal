# messenger/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('enviar_mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
    path('view_message/', views.view_message, name='view_message'),
    path('inbox/', views.inbox, name='inbox'),
    # Agrega más URL para otras vistas como la bandeja de entrada, vista de mensajes, etc.
]
