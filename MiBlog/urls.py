from django.urls import path
from .views import *
from . import views
urlpatterns = [
   
  path('blog/', inicio1, name = 'blog' ),
  path('perfumeriadetalle', perfumeriadetalle, name = 'perfumeriadetalle' ),
  path('dejar_mensaje/', views.dejar_mensaje, name='dejar_mensaje'),
  path('leer_comentario/', views.leer_comentario, name='leer_comentario'),
]


