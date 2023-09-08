from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class perfumeria_Formulario(forms.Form):
    Codigo = forms.IntegerField()
    Nombre = forms.CharField(max_length=50)
    Sexo = forms.CharField(max_length=50)
    Precio = forms.DecimalField(max_digits=10, decimal_places=2)
    
class cuidado_Corporal_Formulario(forms.Form):
    Codigo = forms.IntegerField()
    Nombre = forms.CharField(max_length=50)
    Sexo = forms.CharField(max_length=50)
    Precio = forms.DecimalField(max_digits=10, decimal_places=2)
    
class maquillaje_Formulario(forms.Form):
    Codigo = forms.IntegerField()
    Nombre = forms.CharField(max_length=50)
    Precio = forms.DecimalField(max_digits=10, decimal_places=2)
    
class cabello_Formulario(forms.Form):
    Codigo = forms.IntegerField()
    Nombre = forms.CharField(max_length=50)
    Sexo = forms.CharField(max_length=50)
    Precio = forms.DecimalField(max_digits=10, decimal_places=2)
    
class clientes_Formulario(forms.Form):
    Apellido = forms.CharField(max_length=50)
    Nombre = forms.CharField(max_length=50)
    DNI = forms.CharField(max_length=50)
    Email = forms.EmailField()
    
class RegistroUsuario_Formulario(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username', "password1", "password2"]
        help_texts= {k:"" for k in fields} 
        
class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Email Usuario")
    password1=forms.CharField(label="Contraseña Usuario", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    
    class Meta:
        model=User
        fields=['email', "password1", "password2", "first_name", "last_name"]
        help_texts= {k:"" for k in fields} 
    