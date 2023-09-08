from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Perfumeria(models.Model):
    Codigo = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=50)
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f'{self.Codigo} - {self.Nombre} - {self.Sexo} - {self.Precio}'
    
class Cuidadocorporal(models.Model):
    Codigo = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=50)
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f'{self.Codigo} - {self.Nombre} - {self.Sexo} - {self.Precio}'
    
    
class Maquillaje(models.Model):
    Codigo = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f'{self.Codigo} - {self.Nombre} - {self.Precio}'
    
    
class Cabello(models.Model):
    Codigo = models.IntegerField()
    Nombre = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=50)
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f'{self.Codigo} - {self.Nombre} - {self.Sexo} - {self.Precio}'
    
    
class Clientes(models.Model):
    Apellido = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)
    DNI = models.CharField(max_length=50)
    Email = models.EmailField()
    def __str__(self):
        return f'{self.Apellido} - {self.Nombre} - {self.DNI} -{self.Email}'
    
    
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatars", null=True, blank= True)
    
    
    