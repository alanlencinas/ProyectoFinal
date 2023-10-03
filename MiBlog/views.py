from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from AppCoder.views import obtenerAvatar
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required



def inicio1(request):
    mensaje_form=MensajeForm()
    return render(request, 'MiBlog/blog.html', {"avatar": obtenerAvatar(request), 'mensaje_form': mensaje_form, 'mensajes': Mensaje.objects.all().order_by('-fecha_publicacion')[:10]})

def perfumeriadetalle(request):
    return render(request, "MiBlog/perfumeriadetalle.html", {"avatar": obtenerAvatar(request)})

def maquillajedetalle(request):
    return render(request, "MiBlog/maquillajedetalle.html", {"avatar": obtenerAvatar(request)})

def cabellodetalle(request):
    return render(request, "MiBlog/cabellodetalle.html", {"avatar": obtenerAvatar(request)})


@login_required
def dejar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.autor = request.user  # Asigna el autor del mensaje
            mensaje.save()  # Guarda el mensaje en la base de datos
            form=MensajeForm()
            return redirect('blog')  # Redirige a la página del blog después de dejar el mensaje
    else:
        form = MensajeForm()

    return render(request, 'blog', {'form': form})

def blog(request):
    mensaje_form = MensajeForm()
    mensajes = Mensaje.objects.all().order_by('-fecha_publicacion')[:10]
    return render(request, 'MiBlog/blog.html', {'mensaje_form': mensaje_form, 'mensajes': mensajes, 'avatar': obtenerAvatar(request)})



from django.shortcuts import render, redirect, get_object_or_404

def eliminar_comentario(request, comentario_id):
    # Obtén el comentario o muestra un error 404 si no existe
    comentario = get_object_or_404(Mensaje, pk=comentario_id)

    # Verifica si el usuario actual es un superusuario o tiene permisos para eliminar
    if request.user.is_superuser:
        comentario.delete()
        # Redirige a la página de comentarios después de eliminar
        return redirect('blog')  # Cambia 'blog' al nombre de tu vista de comentarios

    # Si el usuario no es un superusuario, muestra un mensaje de error o redirige a otra página
    # Aquí puedes personalizar el comportamiento según tus necesidades

    return redirect('blog')  # Cambia 'blog' al nombre de tu vista de comentarios o a una página de error

def aboutme(request):
    return render(request, 'MiBlog/aboutme.html', {'avatar': obtenerAvatar(request)})
