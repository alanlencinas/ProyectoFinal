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

from django.contrib.auth.decorators import login_required

@login_required
def dejar_comentario(request, post_id):
    # Obtiene el post al que se va a dejar el comentario

    if request.method == 'POST':
        mensaje_form = MensajeForm(request.POST)
        if mensaje_form.is_valid():
            contenido = mensaje_form.cleaned_data['contenido']
            mensaje = mensaje_form.save(commit=False)
            mensaje.autor = request.user
            mensaje.post = post  # Asigna el post al que se relaciona el comentario
            mensaje.save()
            return redirect('leer_comentario', post_id=post_id)
        else:
            print(mensaje_form.errors)
    else:
        mensaje_form = MensajeForm()

    # Puedes obtener los comentarios asociados al post para mostrarlos
    comentarios = Mensaje.objects.filter(post=post)

    return render(request, 'MiBlog/blog.html', {'mensaje_form': mensaje_form, 'comentarios': comentarios})


@login_required
def leer_comentario(request):
    mensajes = Mensaje.objects.all().order_by('-fecha_publicacion')
    mensaje_form=MensajeForm()
    return render(request, 'MiBlog/blog.html', {'mensajes': mensajes, 'mensaje_form': mensaje_form})