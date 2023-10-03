from django.urls import path
from .views import *
from . import views
urlpatterns = [
   
  path('blog/', inicio1, name = 'blog' ),
  path('perfumeriadetalle', perfumeriadetalle, name = 'perfumeriadetalle' ),
  path('dejar_mensaje/', views.dejar_mensaje, name='dejar_mensaje'),
  path('eliminar_comentario/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario'),
  path('aboutme/', aboutme, name='aboutme'),
  path('maquillaje', maquillajedetalle, name = 'maquillajedetalle' ),
]


