from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.views import obtenerAvatar
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required



def inicio1(request):
    mensaje_form=MensajeForm()
    return render(request, 'MiBlog/blog.html', {"avatar": obtenerAvatar(request), 'mensaje_form': mensaje_form})

def perfumeriadetalle(request):
    return render(request, "MiBlog/perfumeriadetalle.html", {"avatar": obtenerAvatar(request)})


@login_required
def dejar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.autor = request.user  # Asigna el autor del mensaje
            mensaje.save()  # Guarda el mensaje en la base de datos
            form=MensajeForm()
            return redirect('MiBlog/blog.html', {'mensaje_form': form})  # Redirige a la página del blog después de dejar el mensaje
    else:
        form = MensajeForm()

    return render(request, 'MiBlog/blog.html', {'form': form})




@login_required
def leer_comentario(request):
    comentarios = Mensaje.objects.all()
    return render(request, 'MiBlog/blog.html', {'mensajes': comentarios})