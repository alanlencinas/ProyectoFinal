from django.contrib import admin
from .models import Perfumeria, Cabello, Clientes, Maquillaje, Cuidadocorporal, Avatar

# Register your models here.
admin.site.register(Perfumeria)
admin.site.register(Clientes)
admin.site.register(Maquillaje)
admin.site.register(Cabello)
admin.site.register(Cuidadocorporal)
admin.site.register(Avatar)