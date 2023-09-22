# messenger/models.py
from django.db import models
from django.contrib.auth.models import User

class Mensajeria(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajesenviados')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajesrecibidos')
    contenido = models.TextField()
    asunto = models.TextField(default='Sin Asunto')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensaje de {self.emisor} para {self.receptor} de asunto {self.asunto} ({self.timestamp})"
